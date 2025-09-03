# COPR Setup Instructions for libvhdi

This document provides step-by-step instructions for setting up the libvhdi COPR repository.

## Prerequisites

1. **Fedora Account System (FAS) Account**
   - Create at: https://accounts.fedoraproject.org/
   - Required for COPR access

2. **GitHub Account**
   - Push this repository to your GitHub

## Step 1: Push to GitHub

```bash
cd /home/user/libvhdi-copr

# Add all files
git add .

# Commit
git commit -m "Initial commit: libvhdi COPR for Fedora"

# Add your GitHub remote (replace YOUR_GITHUB_USERNAME)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/libvhdi-copr.git

# Push to GitHub
git push -u origin master
```

## Step 2: COPR Web Interface Setup

### Login to COPR
1. Navigate to https://copr.fedorainfracloud.org/
2. Click "Log In" (top right)
3. Use your FAS credentials

### Create New Project

1. Click **"New Project"** button

2. **Fill in Project Information:**

```
Project Name: libvhdi
Description: libvhdi library and tools for Virtual Hard Disk (VHD) format - Required for Xen Orchestra VHD operations
Homepage: https://github.com/libyal/libvhdi
Contact: [your-email]
```

3. **Instructions Field:**
```
Installation:
sudo dnf copr enable YOUR_FAS_USERNAME/libvhdi
sudo dnf install libvhdi-tools
```

4. **Select Chroots (Build Targets):**
   - ✅ fedora-40-x86_64
   - ✅ fedora-41-x86_64
   - ✅ fedora-42-x86_64
   - ✅ fedora-rawhide-x86_64

5. Click **"Create"**

## Step 3: Add Package to Project

1. Navigate to your project: `YOUR_FAS_USERNAME/libvhdi`
2. Click **"Packages"** tab
3. Click **"New Package"**

4. **Fill in Package Settings:**

| Field | Value |
|-------|-------|
| **Package name** | `libvhdi` |
| **Clone URL** | `https://github.com/YOUR_GITHUB_USERNAME/libvhdi-copr.git` |
| **Committish** | `master` (or `main` if you changed branch name) |
| **Subdirectory** | (leave empty) |
| **Spec File** | (leave empty) |
| **Type** | `make srpm` |
| **Build dependencies** | (leave empty) |

5. Click **"Save"**

## Step 4: Trigger First Build

1. On the package page, click **"Rebuild"**
2. Select all Fedora chroots:
   - fedora-40-x86_64
   - fedora-41-x86_64
   - fedora-42-x86_64
   - fedora-rawhide-x86_64
3. Click **"Submit"**

## Step 5: Monitor Build

- Build will take 5-10 minutes
- Status shows on the Builds tab
- Green = Success
- Red = Failed (check build.log)

## Step 6: Test Installation

Once build succeeds:

```bash
# Enable your COPR (replace YOUR_FAS_USERNAME)
sudo dnf copr enable YOUR_FAS_USERNAME/libvhdi

# Install packages
sudo dnf install libvhdi-tools

# Test
vhdiinfo -V
```

## Automation Options

### Enable Auto-rebuild
1. Go to Settings → Integrations
2. Enable GitHub webhook for automatic rebuilds on push

### Package Updates
To update libvhdi version:
1. Edit `.copr/Makefile` - change `VERSION`
2. Commit and push to GitHub
3. COPR auto-rebuilds if webhook enabled, or manually trigger rebuild

## Troubleshooting

### Build Fails
- Click on the failed build
- Check `build.log` for errors
- Common issues:
  - Missing dependencies
  - Network timeout downloading source
  - Spec file syntax errors

### Source Download Issues
- COPR builder must be able to reach GitHub
- Check VERSION in .copr/Makefile matches available release

### Permission Denied
- Ensure you're logged in
- Check you own the project

## Integration with XO Installer

Once COPR is working:

1. Users can install libvhdi:
```bash
sudo dnf copr enable YOUR_FAS_USERNAME/libvhdi
sudo dnf install libvhdi-tools
```

2. Then run modified XO installer:
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/XenOrchestraInstallerUpdater
cd XenOrchestraInstallerUpdater
sudo bash xo-install.sh --install
```

## Advanced: Building libyal Bundle

For future enhancement with full libyal support:

1. Create new spec: `libyal-bundle.spec`
2. Download all libyal dependencies
3. Build in correct order
4. Currently not implemented - single tarball approach works

## Repository Structure

```
libvhdi-copr/
├── .copr/
│   └── Makefile         # COPR reads this for build instructions
├── .gitignore          # Ignore build artifacts
├── libvhdi-simple.spec # Main spec (no Python)
├── build.sh            # Local test script
├── README.md           # User documentation
└── COPR-SETUP.md       # This file
```

## Support Channels

- **COPR Issues**: https://github.com/YOUR_GITHUB_USERNAME/libvhdi-copr/issues
- **COPR Help**: #fedora-buildsys on Libera.Chat IRC
- **Fedora Discourse**: https://discussion.fedoraproject.org/

## Notes

- COPR builds are done in clean chroot environments
- Each Fedora version builds separately
- Rawhide builds may occasionally fail due to dependency changes
- Consider adding EPEL targets if needed for CentOS/RHEL users

## Success Indicators

✅ All builds show green status
✅ Packages installable via dnf
✅ vhdiinfo and vhdimount commands work
✅ XO installer detects libvhdi-tools