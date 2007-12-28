Name: x11-driver-input-mutouch
Version: 1.1.0
Release: %mkrel 5
Summary: X.org input driver for MicroTouch devices
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-input-mutouch-1.1.0@mandriva suggested on upstream
# Tag at git checkout 5e10ff7ecda4df10b6e4d8b7767f5fc64923653e
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-mutouch xorg/drivers/xf86-input-mutouch
# cd xorg/drivers/xf86-input/mutouch
# git-archive --format=tar --prefix=xf86-input-mutouch-1.1.0/ xf86-input-mutouch-1.1.0@mandriva | bzip2 -9 > xf86-input-mutouch-1.1.0.tar.bz2
########################################################################
Source0: xf86-input-mutouch-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-mutouch-1.1.0@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
Mutouch is an X.org input driver for MicroTouch devices.

%package devel
Summary: Development files for %{name}
Group: Development/X11
License: MIT

%description devel
Development files for %{name}

%prep
%setup -q -n xf86-input-mutouch-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# Create list of dependencies
x-check-deps.pl
for deps in *.deps; do
    install -D -m 644 $deps %{buildroot}/%{_datadir}/X11/mandriva/$deps
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/input/mutouch_drv.so
%{_mandir}/man4/mutouch.*

%files devel
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/*.la
%{_datadir}/X11/mandriva/*.deps
