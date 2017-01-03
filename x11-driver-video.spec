#
# Needs more fixes, maybe remove all drivers for non agp/pci cards
# %{sparcx} arch may need more drivers removed, or even better, only
# install sun hardware drivers
#

Name:		x11-driver-video
Version:	1.0.0
Release:	58
Summary:	X11 video drivers
Group:		System/X11
License:	MIT


# useful for qemu
Requires:	x11-driver-video-cirrus
Requires:	x11-driver-video-fbdev
Obsoletes:	x11-driver-video-glint
Obsoletes:	x11-driver-video-geode
%ifnarch %{armx}
Requires:	x11-driver-video-amdgpu
Requires:	x11-driver-video-ati
%endif
# deprecated due of lack of KMS syooirt and no support planned either
Obsoletes:	x11-driver-video-mach64
Requires:	x11-driver-video-mga
Requires:	x11-driver-video-neomagic
%ifnarch %{armx}
Requires:	x11-driver-video-openchrome
%endif
Requires:	x11-driver-video-qxl
Obsoletes:	x11-driver-video-r128
Requires:	x11-driver-video-s3
Obsoletes:	x11-driver-video-s3virge
Requires:	x11-driver-video-savage
Requires:	x11-driver-video-sis
#Not supported by Xorg 13
#Requires:	x11-driver-video-sisimedia
Requires:	x11-driver-video-sisusb
Requires:	x11-driver-video-tdfx
Requires:	x11-driver-video-trident
Obsoletes:	x11-driver-video-v4l
Requires:	x11-driver-video-vesa
Requires:	x11-driver-video-vmware

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

# SGI newport - too uncommon to be installed by default
# Not supported by Xorg 13
#Suggests:	x11-driver-video-newport

Obsoletes:	x11-driver-video-rendition
Suggests:	x11-driver-video-siliconmotion

# DEC Tga - too uncommon to be installed by default
Suggests:	x11-driver-video-tga
Suggests:	x11-driver-video-tseng

# Too old hardware - should not be installed by default
Suggests:	x11-driver-video-voodoo

# Stuff in contrib or recent drivers that nobody might be using:
%ifnarch %{armx}
#Requires:	x11-driver-video-xgi
Suggests:	x11-driver-video-xgixp
%endif

%description uncommon
X11 video drivers metapackage. This package contains no files, but
depends on uncommon free X.org video drivers.

%files uncommon

