Summary:	Xgalaga is a clone of the famouse classic arcade game.
Summary(pl):	Xgalaga to klon bardzo popularnej gry.
Name:		xgalaga 
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www.ibiblio.org/pub/X11/contrib/games/%{name}-%{version}.tar.gz
Patch0:		%{name}-compile.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-score.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xgalaga is a clone of the famouse classic arcade game. Exellent special 
effects make it worth a try espacially if you like a twitch game.

%description -l pl
Xgalaga to klon bardzo popularnej gry. Warto j± wypróbowaæ dla jej wspania³ych
efektów specjalnych :).


%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%define _prefix /usr/X11R6/share/xgalaga
%define _exec_prefix /usr/X11R6/bin
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/games/

%{__make} install DESTDIR=$RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT/var/games/xgalaga.score
gzip -9nf README CHANGES COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,games) %{_exec_prefix}/*
%{_prefix}/*/*
%attr(664,root,games) /var/games/xgalaga.score
