#
# Needs more fixes, maybe remove all drivers for non agp/pci cards
# %{sparcx} arch may need more drivers removed, or even better, only
# install sun hardware drivers
#

Name:		x11-driver-video
Version:	1.0.0
Release:	64
Summary:	X11 video drivers
Group:		System/X11
License:	MIT

Requires:	x11-driver-video-amdgpu
Requires:	x11-driver-video-nouveau

%ifarch %{ix86} %{x86_64}
# useful for qemu
Requires:	x11-driver-video-cirrus
Requires:	x11-driver-video-ati
Requires:	x11-driver-video-fbdev
Requires:	x11-driver-video-mga
Requires:	x11-driver-video-neomagic
Requires:	x11-driver-video-openchrome
Suggests:	x11-driver-video-qxl
Suggests:	x11-driver-video-s3
Suggests:	x11-driver-video-savage
Requires:	x11-driver-video-sis
Suggests:	x11-driver-video-tdfx
Requires:	x11-driver-video-vmware
Requires:	x11-driver-video-vesa
%endif

# deprecated due of lack of KMS support and no support planned either
Obsoletes:	x11-driver-video-mach64
Obsoletes:	x11-driver-video-r128
Obsoletes:	x11-driver-video-s3virge
Obsoletes:	x11-driver-video-v4l
Obsoletes:	x11-driver-video-glint
Obsoletes:	x11-driver-video-geode

%description
X11 video drivers metapackage. This package contains no files, but
depends on most common free X.org video drivers.

%files

%package uncommon
Summary:	Uncommon X11 video drivers
Group:		System/X11
License:	MIT

Suggests:	x11-driver-video-apm
Suggests:	x11-driver-video-ark
Suggests:	x11-driver-video-chips

# Probably only required for development/experiments
Suggests:	x11-driver-video-dummy

Suggests:	x11-driver-video-i128
Suggests:	x11-driver-video-i740

Obsoletes:	x11-driver-video-rendition
Suggests:	x11-driver-video-siliconmotion

# DEC Tga - too uncommon to be installed by default
Suggests:	x11-driver-video-tga
Suggests:	x11-driver-video-tseng

# Too old hardware - should not be installed by default
Suggests:	x11-driver-video-voodoo

# Stuff in contrib or recent drivers that nobody might be using:
%ifnarch %{armx}
Suggests:	x11-driver-video-xgixp
%endif

%description uncommon
X11 video drivers metapackage. This package contains no files, but
depends on uncommon free X.org video drivers.

%files uncommon
