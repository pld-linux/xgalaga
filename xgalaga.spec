Summary:	Xgalaga is a clone of the famous classic arcade game
Summary(pl.UTF-8):	Xgalaga to klon bardzo popularnej gry
Name:		xgalaga
Version:	2.0.34
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/xgalaga/%{name}_%{version}.orig.tar.gz
# Source0-md5:	9f7ee685e9c4741b5f0edc3f91df9510
Patch0:		%{name}-compile.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-score.patch
Patch3:		%{name}-struct.patch
Patch4:		%{name}-libs.patch
URL:		http://rumsey.org/xgal.html
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/xgalaga
%define		_exec_prefix	/usr/bin

%description
Xgalaga is a clone of the famous classic arcade game. Excellent
special effects make it worth a try especially if you like a twitch
game.

%description -l pl.UTF-8
Xgalaga to klon bardzo popularnej gry. Warto ją wypróbować dla jej
wspaniałych efektów specjalnych.

%prep
%setup  -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/games

%{__make} install DESTDIR=$RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT/var/games/xgalaga.score


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(2755,root,games) %{_exec_prefix}/*
%dir %{_prefix}
%{_prefix}/*
%attr(664,root,games) /var/games/xgalaga.score
