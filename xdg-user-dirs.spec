Summary:	Handle user special directories
Summary(pl.UTF-8):	Obsługa specjalnych katalogów użytkownika
Name:		xdg-user-dirs
Version:	0.10
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	6873f49ea7f568743621ed1e05e52dab
Source1:	%{name}.sh
Patch0:		%{name}-configure.patch
URL:		http://www.freedesktop.org/wiki/Software/xdg-user-dirs
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%patch0 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/%{name}.sh

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
        mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh
%attr(755,root,root) %{_bindir}/xdg-user-dir
%attr(755,root,root) %{_bindir}/xdg-user-dirs-update
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/user-dirs.defaults
