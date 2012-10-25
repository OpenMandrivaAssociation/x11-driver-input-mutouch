Name:		x11-driver-input-mutouch
Version:	1.3.0
Release:	5
Summary:	X.org input driver for MicroTouch devices
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-mutouch-%{version}.tar.bz2
License:	MIT
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
Conflicts:	xorg-x11-server < 7.0

Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Mutouch is an X.org input driver for MicroTouch devices.

%prep
%setup -q -n xf86-input-mutouch-%{version}
autoreconf -v --install || exit 1

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/input/mutouch_drv.so
%{_mandir}/man4/mutouch.*
