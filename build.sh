#!/bin/bash
# Build script for libvhdi RPMs on Fedora

set -e

VERSION="20240509"
SPEC_FILE="libvhdi-simple.spec"

echo "=== libvhdi RPM Build Script ==="
echo

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo "This script should not be run as root for building RPMs"
   exit 1
fi

# Install build dependencies if requested
if [[ "$1" == "--install-deps" ]]; then
    echo "Installing build dependencies..."
    sudo dnf install -y \
        gcc make autoconf automake libtool \
        gettext-devel fuse-devel python3-devel \
        python3-setuptools zlib-devel \
        rpm-build rpmdevtools
    echo
fi

# Setup RPM build tree
echo "Setting up RPM build tree..."
rpmdev-setuptree

# Download source if not present
SOURCE_FILE="$HOME/rpmbuild/SOURCES/libvhdi-alpha-${VERSION}.tar.gz"
if [[ ! -f "$SOURCE_FILE" ]]; then
    echo "Downloading libvhdi source tarball..."
    curl -L -o "$SOURCE_FILE" \
        "https://github.com/libyal/libvhdi/releases/download/${VERSION}/libvhdi-alpha-${VERSION}.tar.gz"
else
    echo "Source tarball already present"
fi

# Copy spec file
echo "Copying spec file..."
cp "$SPEC_FILE" "$HOME/rpmbuild/SPECS/"

# Build SRPM
echo "Building SRPM..."
rpmbuild -bs "$HOME/rpmbuild/SPECS/$SPEC_FILE"

# Build RPMs
echo "Building RPMs..."
rpmbuild -bb "$HOME/rpmbuild/SPECS/$SPEC_FILE"

echo
echo "=== Build Complete ==="
echo "RPMs created in: $HOME/rpmbuild/RPMS/x86_64/"
echo
ls -lh "$HOME/rpmbuild/RPMS/x86_64/libvhdi"*.rpm 2>/dev/null | grep -v debuginfo | grep -v debugsource

echo
echo "To install the packages:"
echo "  sudo dnf install $HOME/rpmbuild/RPMS/x86_64/libvhdi-tools-${VERSION}-*.rpm"
echo
echo "For COPR upload:"
echo "  SRPM: $HOME/rpmbuild/SRPMS/libvhdi-${VERSION}-*.src.rpm"