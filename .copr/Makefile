# COPR Makefile for automated builds
# This builds libvhdi from the official release tarball

# Version to build
VERSION = 20240509

# Download URL for the source tarball
TARBALL_URL = https://github.com/libyal/libvhdi/releases/download/$(VERSION)/libvhdi-alpha-$(VERSION).tar.gz

# Default spec file to use (simple version without Python bindings)
SPEC_FILE = libvhdi-simple.spec

# SRPM target is required by COPR
srpm:
	# Ensure we're in the right directory
	test -f ../$(SPEC_FILE) || (echo "Error: $(SPEC_FILE) not found" && exit 1)
	
	# Download the release tarball
	echo "Downloading libvhdi source tarball..."
	curl -L -o libvhdi-alpha-$(VERSION).tar.gz $(TARBALL_URL)
	
	# Copy spec file to current directory
	cp ../$(SPEC_FILE) ./libvhdi.spec
	
	# Create SRPM
	echo "Building SRPM..."
	rpmbuild -bs \
		--define "_sourcedir $(PWD)" \
		--define "_specdir $(PWD)" \
		--define "_builddir $(PWD)" \
		--define "_srcrpmdir $(OUTDIR)" \
		--define "_rpmdir $(PWD)" \
		libvhdi.spec
	
	# Clean up
	rm -f libvhdi.spec libvhdi-alpha-$(VERSION).tar.gz

# Alternative target for building with libyal bundle
srpm-bundle:
	# This would download all libyal dependencies
	# Not implemented yet - requires multiple source files
	echo "Bundle build not yet implemented"

# Clean target for local testing
clean:
	rm -f *.tar.gz *.spec

.PHONY: srpm srpm-bundle clean