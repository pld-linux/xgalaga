Summary:	Xgalaga is a clone of the famous classic arcade game
Summary(pl):	Xgalaga to klon bardzo popularnej gry
Name:		xgalaga
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.mit.edu/afs/athena/contrib/games/src/%{name}-%{version}.tar.gz
# Source0-md5:	ffc1d86b0757a57d23d1cc971014cc43
Patch0:		%{name}-compile.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-score.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/xgalaga
%define		_exec_prefix	/usr/X11R6/bin

%description
Xgalaga is a clone of the famous classic arcade game. Excellent
special effects make it worth a try especially if you like a twitch
game.

%description -l pl
Xgalaga to klon bardzo popularnej gry. Warto j± wypróbowaæ dla jej
wspania³ych efektów specjalnych.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
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
%{_prefix}
%attr(664,root,games) /var/games/xgalaga.score
