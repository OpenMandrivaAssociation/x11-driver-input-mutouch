Summary:	X.org input driver for MicroTouch devices
Name:		x11-driver-input-mutouch
Version:	1.3.0
Release:	18
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mutouch-%{version}.tar.bz2
Patch0:		mutouch-automake-1.13.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Mutouch is an X.org input driver for MicroTouch devices.

%prep
%setup -qn xf86-input-mutouch-%{version}
%apply_patches
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/mutouch_drv.so
%{_mandir}/man4/mutouch.*

