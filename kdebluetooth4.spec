Summary:	KDE Bluetooth framework
Summary(pl.UTF-8):	Podstawowe środowisko KDE Bluetooth
Name:		kdebluetooth4
Version:	0.1
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kde-bluetooth/%{name}-%{version}.tar.bz2
# Source0-md5:	7c6e5162d457fa594ecdd3f339ea8fc1
URL:		http://bluetooth.kmobiletools.org/
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
#BuildRequires:	hgw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDE Bluetooth Framework is a set of tools built on top of Linux'
Bluetooth stack BlueZ. Its goal is to provide easy access to the most
common Bluetooth profiles and to make data exchange with Bluetooth
enabled phones and PDAs as straightforward as possible

%description -l pl.UTF-8
Projekt KDE Bluetooth jest zestawem narzędzi zbudowanych na górnej
warstwie stosu Bluetooth BlueZ. Jego celem jest dostarczenie łatwego
dostępu do większości profili Bluetooth oraz wymiany danych z
telefonami komórkowymi z Bluetooth oraz PDA tak bezpośrednio jak to
jest możliwe.

%prep
%setup -q

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
