Summary:	POSIX Hak
Summary(pl):	POSIX Hak
Name:		posix
Version:	hak
Release:	1
Copyright:	GPL2
Group:		Games/Utility
Group(pl):	Gry/Narzêdzia
Source0:	http://leaf.ultrasoul.com/%{name}-%{version}.tar.gz
# Source0-md5	56f3abe332fc8937ec3d7726010f04da
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
-- empty --

%description -l pl
-- pusty --

%prep
%setup -q

%build
%ifarch ppc
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" CPU="-mpowerpc -maltivect"
%endif
%ifarch %{ix86}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS" CPU="-mcpu=pentium"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install hak unhak itp unitp $RPM_BUILD_ROOT%{_bindir}
%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_bindir}/*
