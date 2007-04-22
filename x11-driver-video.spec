Name: x11-driver-video
Version: 1.0.0
Release: %mkrel 8
Summary: X11 video drivers
Group: System/X11
License: GPL

Requires: x11-driver-video-apm
%ifarch %{ix86}
Requires: x11-driver-video-amd
%endif
Requires: x11-driver-video-ark
Requires: x11-driver-video-ati
Requires: x11-driver-video-chips
Requires: x11-driver-video-cirrus
Requires: x11-driver-video-cyrix
Requires: x11-driver-video-dummy
Requires: x11-driver-video-fbdev
Requires: x11-driver-video-glint
Requires: x11-driver-video-i128
Requires: x11-driver-video-i740
Requires: x11-driver-video-intel
Requires: x11-driver-video-imstt
Requires: x11-driver-video-mga
Requires: x11-driver-video-neomagic
Requires: x11-driver-video-newport
Requires: x11-driver-video-nsc
Requires: x11-driver-video-nv
Requires: x11-driver-video-openchrome
Requires: x11-driver-video-rendition
Requires: x11-driver-video-s3
Requires: x11-driver-video-s3virge
Requires: x11-driver-video-savage
Requires: x11-driver-video-siliconmotion
Requires: x11-driver-video-sis
Requires: x11-driver-video-sisusb
Requires: x11-driver-video-sunbw2
Requires: x11-driver-video-suncg14
Requires: x11-driver-video-suncg3
Requires: x11-driver-video-suncg6
Requires: x11-driver-video-sunffb
Requires: x11-driver-video-sunleo
Requires: x11-driver-video-suntcx
Requires: x11-driver-video-tdfx
Requires: x11-driver-video-tga
Requires: x11-driver-video-trident
Requires: x11-driver-video-tseng
Requires: x11-driver-video-v4l
Requires: x11-driver-video-vesa
Requires: x11-driver-video-vga
Requires: x11-driver-video-via
Requires: x11-driver-video-vmware
Requires: x11-driver-video-voodoo

%description
X11 video drivers

%files
%defattr(-,root,root)



