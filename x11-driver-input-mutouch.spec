%define gitdate %nil

Name: x11-driver-input-mutouch
Version: 1.3.0
Release: 3%{?gitdate:.%{gitdate}}
Summary: X.org input driver for MicroTouch devices
Group: System/X11
URL: http://xorg.freedesktop.org
%if 0%{?gitdate}
Source0: xf86-input-mutouch-%{gitdate}.tar.bz2
%else
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mutouch-%{version}.tar.bz2
%endif
License: MIT
Patch0: mutouch-automake-1.13.patch
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Mutouch is an X.org input driver for MicroTouch devices.

%prep
%if 0%{gitdate}
%setup -q -n xf86-input-mutouch-%{gitdate}
%else
%setup -q -n xf86-input-mutouch-%{version}
%endif
%apply_patches

%build
autoreconf -v --install || exit 1
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/mutouch_drv.so
%{_mandir}/man4/mutouch.*


%changelog
* Tue Jun 28 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.3.0-1.mdv2011.0
+ Revision: 687817
- Updated to 1.3.0

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.99-1.20110609
+ Revision: 683745
- Updated to latest git snapshot.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4
+ Revision: 671129
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.1-3mdv2011.0
+ Revision: 595753
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 1.2.1-1mdv2010.1
+ Revision: 486030
- new version 1.2.1
- adopt to new abi

  + Emmanuel Andry <eandry@mandriva.org>
    - use configure2_5x

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix group

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265870
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194284
- Update to version 1.2.0.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-7mdv2008.1
+ Revision: 160491
- Revert to use only upstream tarballs and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-6mdv2008.1
+ Revision: 156586
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-5mdv2008.1
+ Revision: 154959
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-input-mutouch-1.1.0@mandriva suggested on upstream
 Tag at git checkout 5e10ff7ecda4df10b6e4d8b7767f5fc64923653e
 The tag at this moment is considered correct as there are no functional changes
  for more than 2 years, most recent changes being changes/updates to .gitignore
  and .cvsignore.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-4mdv2008.1
+ Revision: 98643
- minor spec cleanup
- build against xserver 1.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:03:02 (31708)
- fill in summary & descriptions for all input drivers

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 19:59:30 (31594)
- Updated drivers for X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

