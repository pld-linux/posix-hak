Summary:	POSIX Hak - tools to manipulate NWN data from the commandline
Summary(pl):	POSIX Hak - narzêdzia do obróbki danych NWN z linii poleceñ
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

%description -l pl
Posix-hak zawiera narzêdzia do obróbki danych NWN z linii poleceñ.
Aktualnie potrafi pakowaæ i rozpakowywaæ pliki HAK oraz modu³y, oraz
wyci±gaæ (ale jeszcze nie kompilowaæ) ITP i pokrewne formaty. Kiedy to
bêdzie gotowe, sprawa bêdzie wygl±daæ lepiej. Potem jedyn± potrzebn±
rzecz± bêdzie jaki¶ rodzaj importu/eksportu MDL do wolnodostêpnego
modelera i byæ mo¿e graficzny edytor map, co wydaje siê naprawdê
trudne do uzyskania przy u¿yciu vima.

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
