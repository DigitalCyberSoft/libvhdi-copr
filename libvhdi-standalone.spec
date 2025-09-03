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
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
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

%package        python3
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3

%description    python3
The %{name}-python3 package contains Python 3 bindings for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
# Configure with bundled dependencies (already included in release tarball)
%configure \
    --disable-static \
    --enable-wide-character-type \
    --enable-python3 \
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

%files python3
%{python3_sitearch}/pyvhdi.so

%changelog
* Thu Jan 09 2025 Fedora COPR Builder - 20240509-1
- Initial standalone build for Fedora 40, 41, 42 and rawhide
- Uses release tarball with bundled dependencies
- Based on upstream libyal/libvhdi