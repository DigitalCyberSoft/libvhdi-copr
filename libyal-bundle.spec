%global giturl https://github.com/libyal

Name:           libyal-bundle
Version:        20240505
Release:        1%{?dist}
Summary:        Bundle of libyal forensics libraries for Fedora

License:        LGPL-3.0-or-later
URL:            %{giturl}

# Core libraries needed by libvhdi
Source0:        %{giturl}/libcerror/releases/download/20240413/libcerror-beta-20240413.tar.gz
Source1:        %{giturl}/libcthreads/releases/download/20240413/libcthreads-alpha-20240413.tar.gz
Source2:        %{giturl}/libcdata/releases/download/20240414/libcdata-alpha-20240414.tar.gz
Source3:        %{giturl}/libclocale/releases/download/20240414/libclocale-alpha-20240414.tar.gz
Source4:        %{giturl}/libcnotify/releases/download/20240414/libcnotify-alpha-20240414.tar.gz
Source5:        %{giturl}/libcsplit/releases/download/20240414/libcsplit-alpha-20240414.tar.gz
Source6:        %{giturl}/libuna/releases/download/20240414/libuna-alpha-20240414.tar.gz
Source7:        %{giturl}/libcfile/releases/download/20240414/libcfile-alpha-20240414.tar.gz
Source8:        %{giturl}/libcpath/releases/download/20240414/libcpath-alpha-20240414.tar.gz
Source9:        %{giturl}/libbfio/releases/download/20240414/libbfio-alpha-20240414.tar.gz
Source10:       %{giturl}/libfcache/releases/download/20240414/libfcache-alpha-20240414.tar.gz
Source11:       %{giturl}/libfdata/releases/download/20240414/libfdata-alpha-20240414.tar.gz
Source12:       %{giturl}/libfguid/releases/download/20240415/libfguid-alpha-20240415.tar.gz
Source13:       %{giturl}/libfvalue/releases/download/20240415/libfvalue-alpha-20240415.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel

%description
This package bundles multiple libyal libraries required for forensics tools
like libvhdi. It includes libcerror, libcthreads, libcdata, and other
supporting libraries.

%package        devel
Summary:        Development files for libyal libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for the libyal bundle libraries.

%prep
# Extract all sources
for i in {0..13}; do
    tar xzf %{_sourcedir}/$(basename %{SOURCE$i})
done

%build
# Build order matters - dependencies first
LIBS="libcerror libcthreads libcdata libclocale libcnotify libcsplit libuna libcfile libcpath libbfio libfcache libfdata libfguid libfvalue"

for lib in $LIBS; do
    cd $lib-*
    %configure --disable-static --prefix=%{_prefix} --libdir=%{_libdir}
    %make_build
    cd ..
done

%install
LIBS="libcerror libcthreads libcdata libclocale libcnotify libcsplit libuna libcfile libcpath libbfio libfcache libfdata libfguid libfvalue"

for lib in $LIBS; do
    cd $lib-*
    %make_install
    cd ..
done

# Remove libtool archives
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*

%changelog
* Thu Jan 09 2025 Fedora COPR Builder - 20240505-1
- Initial bundle of libyal libraries for Fedora
- Includes core dependencies needed by libvhdi and other forensics tools