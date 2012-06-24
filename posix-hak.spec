Summary:	POSIX Hak - tools to manipulate NWN data from the commandline
Summary(pl):	POSIX Hak - narz�dzia do obr�bki danych NWN z linii polece�
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
Posix-hak zawiera narz�dzia do obr�bki danych NWN z linii polece�.
Aktualnie potrafi pakowa� i rozpakowywa� pliki HAK oraz modu�y, oraz
wyci�ga� (ale jeszcze nie kompilowa�) ITP i pokrewne formaty. Kiedy to
b�dzie gotowe, sprawa b�dzie wygl�da� lepiej. Potem jedyn� potrzebn�
rzecz� b�dzie jaki� rodzaj importu/eksportu MDL do wolnodost�pnego
modelera i by� mo�e graficzny edytor map, co wydaje si� naprawd�
trudne do uzyskania przy u�yciu vima.

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
