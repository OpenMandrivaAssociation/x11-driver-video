#
# Needs more fixes, maybe remove all drivers for non agp/pci cards
# sunsparc arch may need more drivers removed, or even better, only
# install sun hardware drivers
#

Name:		x11-driver-video
Version:	1.0.0
Release:	44
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
%ifnarch %{sunsparc} %{arm}
Requires:	x11-driver-video-intel
Requires:	x11-driver-video-nouveau
%endif
Requires:	x11-driver-video-mach64
Requires:	x11-driver-video-mga
Requires:	x11-driver-video-neomagic
Requires:	x11-driver-video-nv
Requires:	x11-driver-video-openchrome
Requires:	x11-driver-video-r128
Requires:	x11-driver-video-s3
Requires:	x11-driver-video-s3virge
Requires:	x11-driver-video-savage
Requires:	x11-driver-video-sis
#Not supported by Xorg 13
#Requires:	x11-driver-video-sisimedia
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

Suggests:	x11-driver-video-rendition
Suggests:	x11-driver-video-siliconmotion

# DEC Tga - too uncommon to be installed by default
Suggests:	x11-driver-video-tga
Suggests:	x11-driver-video-tseng

# Too old hardware - should not be installed by default
Suggests:	x11-driver-video-voodoo

# Stuff in contrib or recent drivers that nobody might be using:
#Requires:	x11-driver-video-xgi
Suggests:	x11-driver-video-xgixp
Suggests:	x11-driver-video-qxl

%description uncommon
X11 video drivers metapackage. This package contains no files, but
depends on uncommon free X.org video drivers.

%files uncommon
%defattr(-,root,root)


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-35mdv2011.0
+ Revision: 671136
- mass rebuild

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.0.0-34mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - Add xgi, xgixp and qxl to -uncommon

* Fri Feb 12 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-32mdv2010.1
+ Revision: 504695
- Don't require vga: doesn't work, unmaintained upstream

* Thu Feb 11 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-31mdv2010.1
+ Revision: 504295
- Don't require i810: it doesn't work. Use vesa or intel.

* Wed Dec 23 2009 Anssi Hannula <anssi@mandriva.org> 1.0.0-30mdv2010.1
+ Revision: 481893
- require x11-driver-video-nouveau

* Tue Aug 11 2009 Funda Wang <fwang@mandriva.org> 1.0.0-29mdv2010.0
+ Revision: 414681
- fix requires on uncommon

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-28mdv2009.1
+ Revision: 308273
- drop now unused drivers cyrix, imstt and viaarena

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-27mdv2009.1
+ Revision: 308208
- no longer require via (replaced totally by openchrome now)

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-26mdv2009.1
+ Revision: 308170
- no longer require nsc (migrated to geode)
- drop the require on amd (nothing uses it now, everything uses geode)

* Mon Nov 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-24mdv2009.1
+ Revision: 306159
- require x11-driver-video-i810 for early i810

* Thu Oct 16 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-23mdv2009.1
+ Revision: 294176
- move back x11-driver-video-via in main package, we still use it (#42909)

* Tue Sep 09 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-22mdv2009.0
+ Revision: 282998
- do not require x11-driver-video-vboxvideo, this is handled in rpmsrate

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-21mdv2009.0
+ Revision: 282695
- requires x11-driver-video-vboxvideo so that it work out of the box in vbox

* Mon Aug 25 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-20mdv2009.0
+ Revision: 276030
- prepare to rename sis-imedia sisimedia (name has to be consistent between
  driver and package or XFdrake fails)

* Mon Aug 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-19mdv2009.0
+ Revision: 270642
- fix requiring x11-driver-video-sis-imedia

* Sun Aug 10 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-18mdv2009.0
+ Revision: 270584
- add sisimedia (required for some semi-common new SiS chips)

* Fri Jul 04 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-17mdv2009.0
+ Revision: 231646
- add back x11-driver-video-cirrus in main package (useful for qemu)

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-16mdv2009.0
+ Revision: 219505
- x11-driver-video-mach64 & x11-driver-video-r128 were splited out of ati driver

* Tue May 20 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-15mdv2009.0
+ Revision: 209529
- put s3 back in the main package, we still have at least a few users with this driver

* Thu May 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.0-14mdv2009.0
+ Revision: 207870
- Don't install by default drivers for isa cards or drivers that did not
  receive an update in around 5 years.
  The new virtual package -uncommon allows installing those.

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-13mdv2009.0
+ Revision: 168306
- fix no-buildroot-tag

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Some updates to avoid installing files that will not be used, or that when
      required, the person installing the OS will know what is required.

* Wed Nov 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-12mdv2008.1
+ Revision: 113543
- bump release
- drop x11-driver-video-avivo requirement, driver is obsolete and i've deleted it

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-11mdv2008.0
+ Revision: 91564
- add radeonhd

* Thu Sep 13 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-10mdv2008.0
+ Revision: 85259
- add viaarena to driver list
- use MIT for license
- expand description
- tabs not spaces

* Tue Aug 14 2007 Thierry Vignaud <tv@mandriva.org> 1.0.0-9mdv2008.0
+ Revision: 63160
- requires x11-driver-video-avivo

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - do not require x11-driver-video-i810 on sparc

* Sun Apr 22 2007 Colin Guthrie <cguthrie@mandriva.org> 1.0.0-8mdv2008.0
+ Revision: 16852
- Update for i810 -> intel rename.


* Tue Mar 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-7mdv2007.1
+ Revision: 146941
- fix installing on x86_64

* Fri Mar 16 2007 Olivier Blin <oblin@mandriva.com> 1.0.0-6mdv2007.1
+ Revision: 144697
- require x11-driver-video-amd (for Geode chipsets)

* Thu Jan 18 2007 Olivier Blin <oblin@mandriva.com> 1.0.0-5mdv2007.1
+ Revision: 110378
- require x11-driver-video-openchrome

* Tue Sep 19 2006 Pixel <pixel@mandriva.com> 1.0.0-4mdv2007.0
+ Revision: 61944
- do not obsolete xorg-x11-server which is still a package in 2007.0

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix group

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

