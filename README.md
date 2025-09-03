# libvhdi COPR for Fedora

This repository provides libvhdi packages for Fedora 40, 41, 42, and rawhide through COPR.

## What is libvhdi?

libvhdi is a library to access the Virtual Hard Disk (VHD) image format, used by:
- Microsoft Hyper-V
- Xen Orchestra (for VHD operations)
- Digital forensics tools
- Virtual disk management utilities

## Quick Installation

Once the COPR repository is active:

```bash
# Enable the COPR repository (replace YOUR_USERNAME with actual username)
sudo dnf copr enable YOUR_USERNAME/libvhdi

# Install libvhdi tools
sudo dnf install libvhdi-tools

# Verify installation
vhdiinfo -V
```

## Repository Contents

- `libvhdi-simple.spec` - Main spec file (standalone build, no Python)
- `libvhdi-standalone.spec` - Alternative with Python support attempt
- `libyal-bundle.spec` - Bundle of libyal libraries (future work)
- `.copr/Makefile` - COPR build automation
- `build.sh` - Local build script for testing

## Building Locally

### Prerequisites

```bash
sudo dnf install -y gcc make autoconf automake libtool \
                    gettext-devel fuse-devel zlib-devel \
                    rpm-build rpmdevtools
```

### Build Process

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/libvhdi-copr
cd libvhdi-copr

# Run the build script
./build.sh

# Or build manually
rpmdev-setuptree
curl -L -o ~/rpmbuild/SOURCES/libvhdi-alpha-20240509.tar.gz \
     https://github.com/libyal/libvhdi/releases/download/20240509/libvhdi-alpha-20240509.tar.gz
cp libvhdi-simple.spec ~/rpmbuild/SPECS/
rpmbuild -bb ~/rpmbuild/SPECS/libvhdi-simple.spec
```

## COPR Setup Instructions

### 1. Create COPR Account
- Go to https://copr.fedorainfracloud.org/
- Sign in with your Fedora Account System (FAS) credentials

### 2. Create New Project
- Click "New Project"
- Fill in the following:

**Basic Information:**
- **Project Name:** `libvhdi`
- **Description:** `libvhdi library and tools for Virtual Hard Disk (VHD) format - Required for Xen Orchestra VHD operations`
- **Homepage:** `https://github.com/libyal/libvhdi`
- **Contact:** Your email
- **Disable build:** Leave unchecked

**Build Options:**
- **Chroots:** Enable:
  - `fedora-40-x86_64`
  - `fedora-41-x86_64`
  - `fedora-42-x86_64`
  - `fedora-rawhide-x86_64`
- **External repositories:** Leave empty
- **Bootstrap:** Leave default
- **Multilib:** Leave unchecked
- **Module hotfixes:** Leave unchecked

### 3. Add Package
After creating the project:
- Go to "Packages" tab
- Click "New Package"

**Package Settings:**
- **Package name:** `libvhdi`
- **Clone URL:** `https://github.com/YOUR_USERNAME/libvhdi-copr.git`
- **Subdirectory:** Leave empty (COPR will find .copr/Makefile)
- **Spec File:** Leave empty (Makefile handles this)
- **Type:** Select `make srpm`
- **Build dependencies:** Leave empty

### 4. Trigger Build
- Click "Rebuild" on the package
- Select desired chroots
- Click "Submit"

## Package Information

### Packages Provided

- **libvhdi** - Main library
  - Shared library for VHD access
  
- **libvhdi-devel** - Development files
  - Headers and pkg-config files
  
- **libvhdi-tools** - Command-line tools
  - `vhdiinfo` - Display VHD file information
  - `vhdimount` - Mount VHD files using FUSE

### Usage Examples

```bash
# Get information about a VHD file
vhdiinfo disk.vhd

# Mount a VHD file
mkdir /mnt/vhd
vhdimount disk.vhd /mnt/vhd
ls /mnt/vhd/

# Unmount
fusermount -u /mnt/vhd
```

## Integration with Xen Orchestra

This package is designed to work with the modified XenOrchestraInstallerUpdater for Fedora:

1. Install libvhdi-tools from this COPR
2. Run the modified XO installer
3. XO will detect and use vhdimount for VHD operations

## Known Issues

- Python bindings are currently disabled due to path issues
- Only x86_64 architecture is supported
- Some VHD operations in XO may work without libvhdi, but functionality will be limited

## Contributing

To update the package:

1. Fork this repository
2. Update `VERSION` in `.copr/Makefile`
3. Test locally with `build.sh`
4. Commit and push changes
5. COPR will automatically rebuild

## License

libvhdi is licensed under LGPL-3.0-or-later

## Support

- **COPR Issues:** Open issue in this repository
- **libvhdi Issues:** Report upstream at https://github.com/libyal/libvhdi/issues
- **XO Installer:** See https://github.com/ronivay/XenOrchestraInstallerUpdater

## Related Projects

- [XenOrchestraInstallerUpdater](https://github.com/ronivay/XenOrchestraInstallerUpdater) - XO installer (needs Fedora support PR)
- [libyal/libvhdi](https://github.com/libyal/libvhdi) - Upstream libvhdi
- [Xen Orchestra](https://github.com/vatesfr/xen-orchestra) - The actual XO project

## Changelog

### 20240509-1
- Initial release for Fedora 40, 41, 42, and rawhide
- Based on upstream libvhdi-alpha-20240509
- Python bindings disabled (build issues)
- Includes vhdiinfo and vhdimount tools