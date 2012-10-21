#
# Needs more fixes, maybe remove all drivers for non agp/pci cards
# sparcx arch may need more drivers removed, or even better, only
# install sun hardware drivers
#

Name:		x11-driver-video
Version:	1.0.0
Release:	37
Summary:	X11 video drivers
Group:		System/X11
License:	MIT

Requires:	x11-driver-video-ati
# useful for qemu
Requires:	x11-driver-video-cirrus
Requires:	x11-driver-video-fbdev
Requires:	x11-driver-video-glint
%ifarch %{ix86}
Requires:	x11-driver-video-geode
%endif
%ifnarch %{sparcx}
Requires:	x11-driver-video-intel
%endif
Requires:	x11-driver-video-mach64
Requires:	x11-driver-video-mga
Requires:	x11-driver-video-neomagic
Requires:	x11-driver-video-nouveau
Requires:	x11-driver-video-nv
Requires:	x11-driver-video-openchrome
Requires:	x11-driver-video-r128
Requires:	x11-driver-video-s3
Requires:	x11-driver-video-s3virge
Requires:	x11-driver-video-savage
Requires:	x11-driver-video-sis
Requires:	x11-driver-video-sisimedia
Requires:	x11-driver-video-sisusb
%ifarch %{sparcx}
Requires:	x11-driver-video-sunbw2
Requires:	x11-driver-video-suncg14
Requires:	x11-driver-video-suncg3
Requires:	x11-driver-video-suncg6
Requires:	x11-driver-video-sunffb
Requires:	x11-driver-video-sunleo
Requires:	x11-driver-video-suntcx
%endif
Requires:	x11-driver-video-tdfx
Requires:	x11-driver-video-trident
Requires:	x11-driver-video-v4l
Requires:	x11-driver-video-vesa
Requires:	x11-driver-video-vmware

%description
X11 video drivers metapackage. This package contains no files, but
depends on most common free X.org video drivers.

%files

%package	uncommon
Summary:	Uncommon X11 video drivers
Group:		System/X11
License:	MIT
Requires:	x11-driver-video-apm
Requires:	x11-driver-video-ark
Requires:	x11-driver-video-chips

# Probably only required for development/experiments
Requires:	x11-driver-video-dummy

Requires:	x11-driver-video-i128
Requires:	x11-driver-video-i740

# SGI newport - too uncommon to be installed by default
Requires:	x11-driver-video-newport

Requires:	x11-driver-video-rendition
Requires:	x11-driver-video-siliconmotion

# DEC Tga - too uncommon to be installed by default
Requires:	x11-driver-video-tga
Requires:	x11-driver-video-tseng

# Too old hardware - should not be installed by default
Requires:	x11-driver-video-voodoo

# Stuff in contrib or recent drivers that nobody might be using:
Requires:	x11-driver-video-xgi
Requires:	x11-driver-video-xgixp
Requires:	x11-driver-video-qxl

%description	uncommon
X11 video drivers metapackage. This package contains no files, but
depends on uncommon free X.org video drivers.

%files		uncommon
