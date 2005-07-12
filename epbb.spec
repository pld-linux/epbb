Summary:	pbbuttonsd client using EFL
Summary(pl):	Klient pbbuttonsd u¿ywaj±cy EFL
Name:		epbb
Version:	0.0.5
%define	_snap	20050701
Release:	0.%{_snap}.0.3
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/misc/%{name}-%{_snap}.tar.gz
# Source0-md5:	997c060d20720caba7f7d30a24fc5042
Source1:	%{name}-metalsphere.png
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	edje-devel
BuildRequires:	evas-devel
BuildRequires:	libtool
BuildRequires:	pbbuttonsd-lib
BuildRequires:	sed >= 4.0
Requires:	fonts-TTF-bitstream-vera
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pbbuttonsd client using EFL. Only thing it can do is checking battery
status.

%description -l pl
Klient pbbuttonsd u¿ywaj±cy EFL. Jedyne co potrafi to sprawdzanie
stanu baterii.

%prep
%setup -q -n %{name}
install %{SOURCE1} data/images/metalsphere.png
sed 's/ipc_init(LIBMODE_CLIENT, 1)/ipc_init("epbb", LIBMODE_CLIENT, 1)/' \
	-i src/bin/main.c

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
VERA=$(ls Vera*.ttf)
for FONT in $VERA; do
	rm -f $FONT
	ln -s %{_fontsdir}/TTF/$FONT .
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
