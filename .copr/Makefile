# COPR Makefile for automated builds
# This is self-contained - generates spec file and downloads source

# Version to build
VERSION = 20240509

# Download URL for the source tarball
TARBALL_URL = https://github.com/libyal/libvhdi/releases/download/$(VERSION)/libvhdi-alpha-$(VERSION).tar.gz

# SRPM target is required by COPR
srpm:
	@echo "Starting libvhdi SRPM build for version $(VERSION)"
	
	# Download the release tarball
	@echo "Downloading libvhdi source tarball..."
	curl -L -o libvhdi-alpha-$(VERSION).tar.gz $(TARBALL_URL)
	
	# Generate the spec file using echo commands
	@echo "Generating spec file..."
	@echo '%global giturl https://github.com/libyal/libvhdi' > libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo 'Name:           libvhdi' >> libvhdi.spec
	@echo 'Version:        $(VERSION)' >> libvhdi.spec
	@echo 'Release:        1%{?dist}' >> libvhdi.spec
	@echo 'Summary:        Library to access the Virtual Hard Disk (VHD) image format' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo 'License:        LGPL-3.0-or-later' >> libvhdi.spec
	@echo 'URL:            %{giturl}' >> libvhdi.spec
	@echo 'Source0:        libvhdi-alpha-%{version}.tar.gz' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo 'BuildRequires:  gcc' >> libvhdi.spec
	@echo 'BuildRequires:  make' >> libvhdi.spec
	@echo 'BuildRequires:  autoconf' >> libvhdi.spec
	@echo 'BuildRequires:  automake' >> libvhdi.spec
	@echo 'BuildRequires:  libtool' >> libvhdi.spec
	@echo 'BuildRequires:  gettext-devel' >> libvhdi.spec
	@echo 'BuildRequires:  fuse-devel >= 2.6' >> libvhdi.spec
	@echo 'BuildRequires:  zlib-devel' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%description' >> libvhdi.spec
	@echo 'libvhdi is a library to access the Virtual Hard Disk (VHD) image format.' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo 'Read support for:' >> libvhdi.spec
	@echo '- Fixed-size hard disk image' >> libvhdi.spec
	@echo '- Dynamic-size (or sparse) hard disk image' >> libvhdi.spec
	@echo '- Differential (or differencing) hard disk image' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo 'This is a standalone build that includes all necessary libyal dependencies' >> libvhdi.spec
	@echo 'bundled internally.' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%package        devel' >> libvhdi.spec
	@echo 'Summary:        Development files for %{name}' >> libvhdi.spec
	@echo 'Requires:       %{name}%{?_isa} = %{version}-%{release}' >> libvhdi.spec
	@echo 'Requires:       pkgconfig' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%description    devel' >> libvhdi.spec
	@echo 'The %{name}-devel package contains libraries and header files for' >> libvhdi.spec
	@echo 'developing applications that use %{name}.' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%package        tools' >> libvhdi.spec
	@echo 'Summary:        Command line tools for %{name}' >> libvhdi.spec
	@echo 'Requires:       %{name}%{?_isa} = %{version}-%{release}' >> libvhdi.spec
	@echo 'Requires:       fuse-libs >= 2.6' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%description    tools' >> libvhdi.spec
	@echo 'The %{name}-tools package contains command line tools for %{name}:' >> libvhdi.spec
	@echo '- vhdiinfo: shows information about VHD files' >> libvhdi.spec
	@echo '- vhdimount: FUSE mounts VHD files' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%prep' >> libvhdi.spec
	@echo '%autosetup -n %{name}-%{version}' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%build' >> libvhdi.spec
	@echo '# Configure with bundled dependencies (already included in release tarball)' >> libvhdi.spec
	@echo '# Disable Python bindings for now as they have path issues' >> libvhdi.spec
	@echo '%configure \' >> libvhdi.spec
	@echo '    --disable-static \' >> libvhdi.spec
	@echo '    --enable-wide-character-type \' >> libvhdi.spec
	@echo '    --disable-python \' >> libvhdi.spec
	@echo '    --with-zlib \' >> libvhdi.spec
	@echo '    --with-libfuse' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%make_build' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%install' >> libvhdi.spec
	@echo '%make_install' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '# Remove libtool archives' >> libvhdi.spec
	@echo "find %{buildroot} -name '*.la' -delete" >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%ldconfig_scriptlets' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%files' >> libvhdi.spec
	@echo '%license COPYING COPYING.LESSER' >> libvhdi.spec
	@echo '%doc AUTHORS README' >> libvhdi.spec
	@echo '%{_libdir}/*.so.*' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%files devel' >> libvhdi.spec
	@echo '%{_includedir}/*' >> libvhdi.spec
	@echo '%{_libdir}/*.so' >> libvhdi.spec
	@echo '%{_libdir}/pkgconfig/*.pc' >> libvhdi.spec
	@echo '%{_mandir}/man3/*.3*' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%files tools' >> libvhdi.spec
	@echo '%{_bindir}/vhdiinfo' >> libvhdi.spec
	@echo '%{_bindir}/vhdimount' >> libvhdi.spec
	@echo '%{_mandir}/man1/*.1*' >> libvhdi.spec
	@echo '' >> libvhdi.spec
	@echo '%changelog' >> libvhdi.spec
	@echo '* Thu Jan 09 2025 COPR Builder - $(VERSION)-1' >> libvhdi.spec
	@echo '- Automated build from COPR' >> libvhdi.spec
	@echo '- Based on upstream libyal/libvhdi release tarball' >> libvhdi.spec
	@echo '- Python bindings disabled (path issues)' >> libvhdi.spec
	
	# Create SRPM
	@echo "Building SRPM..."
	rpmbuild -bs \
		--define "_sourcedir $(PWD)" \
		--define "_specdir $(PWD)" \
		--define "_builddir $(PWD)" \
		--define "_srcrpmdir $(OUTDIR)" \
		--define "_rpmdir $(PWD)" \
		libvhdi.spec
	
	@echo "SRPM build complete"

# Clean target for local testing
clean:
	rm -f *.tar.gz *.spec *.src.rpm

.PHONY: srpm clean