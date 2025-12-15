Summary:	Handle user special directories
Summary(pl.UTF-8):	Obsługa specjalnych katalogów użytkownika
Name:		xdg-user-dirs
Version:	0.19
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	0307f432c7f80a196061ee3466304acf
Source1:	%{name}.sh
Patch0:		%{name}-am.patch
URL:		https://www.freedesktop.org/wiki/Software/xdg-user-dirs
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	gettext-tools >= 0.14.4
BuildRequires:	libxslt-progs
BuildRequires:	rpmbuild(macros) >= 1.682
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%description -l pl.UTF-8
xdg-user-dirs to narzędzie pomagające zarządzać "dobrze znanymi"
katalogami użytkownika, takimi jak pulpit czy katalog z muzyką.
Obsługuje także lokalizację (tzn. tłumaczenia) nazw plików.

%prep
%setup -q
%patch -P0 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/%{name}.sh

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md TODO
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh
%attr(755,root,root) %{_bindir}/xdg-user-dir
%attr(755,root,root) %{_bindir}/xdg-user-dirs-update
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/user-dirs.defaults
%{_sysconfdir}/xdg/autostart/xdg-user-dirs.desktop
%{systemduserunitdir}/xdg-user-dirs.service
%{_mandir}/man1/xdg-user-dir.1*
%{_mandir}/man1/xdg-user-dirs-update.1*
%{_mandir}/man5/user-dirs.conf.5*
%{_mandir}/man5/user-dirs.defaults.5*
%{_mandir}/man5/user-dirs.dirs.5*
