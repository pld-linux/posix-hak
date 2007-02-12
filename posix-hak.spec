Summary:	POSIX Hak - tools to manipulate NWN data from the commandline
Summary(pl.UTF-8):   POSIX Hak - narzędzia do obróbki danych NWN z linii poleceń
Name:		posix-hak
Version:	0
Release:	1
License:	GPL v2
Group:		Applications/Games
Source0:	http://www.ultrasoul.com/%7Eleaf/%{name}.tar.gz
# Source0-md5	56f3abe332fc8937ec3d7726010f04da
URL:		http://www.ultrasoul.com/~leaf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Posix-hak contains some tools to manipulate NWN data from the
commandline. Currently packs and unpacks HAKs and Modules, and
extracts (but not yet compiles) the ITP and related formats. When that
is done things will be looking on the up and up. After that the only
thing needed will be some sort of MDL import/export for a free modeler
and maybe a GUI map editor, as it seems to be really hard to get them
right with vim.

%description -l pl.UTF-8
Posix-hak zawiera narzędzia do obróbki danych NWN z linii poleceń.
Aktualnie potrafi pakować i rozpakowywać pliki HAK oraz moduły, oraz
wyciągać (ale jeszcze nie kompilować) ITP i pokrewne formaty. Kiedy to
będzie gotowe, sprawa będzie wyglądać lepiej. Potem jedyną potrzebną
rzeczą będzie jakiś rodzaj importu/eksportu MDL do wolnodostępnego
modelera i być może graficzny edytor map, co wydaje się naprawdę
trudne do uzyskania przy użyciu vima.

%prep
%setup -q -n %{name}

%build
# leave CPU empty to use just rpmcflags
%{__make} \
	CC="%{__cc}" \
	CPU= \
	OPTIMIZE="%{rpmcflags}" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install hak unhak itp unitp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
