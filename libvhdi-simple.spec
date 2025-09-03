%global giturl https://github.com/libyal/libvhdi

Name:           libvhdi
Version:        20240509
Release:        1%{?dist}
Summary:        Library to access the Virtual Hard Disk (VHD) image format

License:        LGPL-3.0-or-later
URL:            %{giturl}
Source0:        %{giturl}/releases/download/%{version}/libvhdi-alpha-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make  
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  fuse-devel >= 2.6
BuildRequires:  zlib-devel

%description
libvhdi is a library to access the Virtual Hard Disk (VHD) image format.

Read support for:
- Fixed-size hard disk image
- Dynamic-size (or sparse) hard disk image  
- Differential (or differencing) hard disk image

This is a standalone build that includes all necessary libyal dependencies
bundled internally.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fuse-libs >= 2.6

%description    tools
The %{name}-tools package contains command line tools for %{name}:
- vhdiinfo: shows information about VHD files
- vhdimount: FUSE mounts VHD files

%prep
%autosetup -n %{name}-%{version}

%build
# Configure with bundled dependencies (already included in release tarball)
# Disable Python bindings for now as they have path issues
%configure \
    --disable-static \
    --enable-wide-character-type \
    --disable-python \
    --with-zlib \
    --with-libfuse

%make_build

%install
%make_install

# Remove libtool archives
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets

%files
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*

%files tools
%{_bindir}/vhdiinfo
%{_bindir}/vhdimount
%{_mandir}/man1/*.1*

%changelog
* Thu Jan 09 2025 Fedora COPR Builder - 20240509-1
- Initial build for Fedora 40, 41, 42 and rawhide
- Uses release tarball with bundled dependencies
- Based on upstream libyal/libvhdi
- Python bindings disabled for now