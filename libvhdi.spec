%global giturl https://github.com/libyal/libvhdi
%global commit main

Name:           libvhdi
Version:        20240505
Release:        1%{?dist}
Summary:        Library to access the Virtual Hard Disk (VHD) image format

License:        LGPL-3.0-or-later
URL:            %{giturl}
Source0:        %{giturl}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  libcerror-devel >= 20120425
BuildRequires:  libcthreads-devel >= 20130724
BuildRequires:  libcdata-devel >= 20140105
BuildRequires:  libclocale-devel >= 20120425
BuildRequires:  libcnotify-devel >= 20120425
BuildRequires:  libcsplit-devel >= 20120701
BuildRequires:  libuna-devel >= 20120425
BuildRequires:  libcfile-devel >= 20120526
BuildRequires:  libcpath-devel >= 20120701
BuildRequires:  libbfio-devel >= 20120426
BuildRequires:  libfcache-devel >= 20120405
BuildRequires:  libfdata-devel >= 20120405
BuildRequires:  libfguid-devel >= 20120426
BuildRequires:  libfvalue-devel >= 20120428
BuildRequires:  libfuse-devel >= 2.6
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
libvhdi is a library to access the Virtual Hard Disk (VHD) image format.

Read support for:
- Fixed-size hard disk image
- Dynamic-size (or sparse) hard disk image  
- Differential (or differencing) hard disk image
  - Note that an undo disk image (.vud) is also a differential image

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
Requires:       libfuse >= 2.6

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
%autosetup -n %{name}-%{commit}

# Generate build system
./synclibs.sh
./autogen.sh

%build
%configure \
    --disable-static \
    --enable-wide-character-type \
    --enable-python3

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
* Thu Jan 09 2025 Fedora COPR Builder - 20240505-1
- Initial build for Fedora 40, 41, 42 and rawhide
- Based on upstream libyal/libvhdi
- Adapted from EPEL packaging