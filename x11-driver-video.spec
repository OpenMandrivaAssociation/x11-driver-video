#
# Needs more fixes, maybe remove all drivers for non agp/pci cards
# sunsparc arch may need more drivers removed, or even better, only
# install sun hardware drivers
#

Name:		x11-driver-video
Version:	1.0.0
Release:	%mkrel 21
Summary:	X11 video drivers
Group:		System/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	MIT

%ifarch %{ix86}
Requires:	x11-driver-video-amd
%endif
Requires:	x11-driver-video-ati
# useful for qemu
Requires:	x11-driver-video-cirrus
Requires:	x11-driver-video-fbdev
Requires:	x11-driver-video-glint
%ifarch %{ix86}
Requires:	x11-driver-video-geode
%endif
%ifnarch %{sunsparc}
Requires:	x11-driver-video-intel
%endif
Requires:	x11-driver-video-mach64
Requires:	x11-driver-video-mga
Requires:	x11-driver-video-neomagic
Requires:	x11-driver-video-nsc
Requires:	x11-driver-video-nv
Requires:	x11-driver-video-openchrome
Requires:	x11-driver-video-radeonhd
Requires:	x11-driver-video-r128
Requires:	x11-driver-video-s3
Requires:	x11-driver-video-s3virge
Requires:	x11-driver-video-savage
Requires:	x11-driver-video-sis
Requires:	x11-driver-video-sisimedia
Requires:	x11-driver-video-sisusb
%ifarch %{sunsparc}
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
Requires:	x11-driver-video-vboxvideo
Requires:	x11-driver-video-vga
Requires:	x11-driver-video-vmware

%description
X11 video drivers metapackage. This package contains no files, but
depends on most common free X.org video drivers.

%files
%defattr(-,root,root)

%package uncommon
Summary:	Uncommon X11 video drivers
Group:		System/X11
License:	MIT

%description uncommon
X11 video drivers metapackage. This package contains no files, but
depends on uncommon free X.org video drivers.

Requires:	x11-driver-video-apm
Requires:	x11-driver-video-ark
Requires:	x11-driver-video-chips
Requires:	x11-driver-video-cyrix

# Probably only required for development/experiments
Requires:	x11-driver-video-dummy

Requires:	x11-driver-video-i128
Requires:	x11-driver-video-i740
Requires:	x11-driver-video-imstt

# SGI newport - too uncommon to be installed by default
Requires:	x11-driver-video-newport

Requires:	x11-driver-video-rendition
Requires:	x11-driver-video-siliconmotion

# DEC Tga - too uncommon to be installed by default
Requires:	x11-driver-video-tga
Requires:	x11-driver-video-tseng

# Openchrome should make these obsolete
Requires:	x11-driver-video-via
Requires:	x11-driver-video-viaarena

# Too old hardware - should not be installed by default
Requires:	x11-driver-video-voodoo

%files uncommon
%defattr(-,root,root)
