Summary:	The original mozilla skin, used defore the creation of the Modern 1.
Summary(pl):	Oryginalna skórka Mozilli, u¿ywana przed utworzeniem Modern 1.
Name:		mozilla-theme-EarlyBlue
%define		_realname	EarlyBlue
Version:	1.0
%define	fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.hirsch.sth.ac.at/~robert/kairo.at/dl/%{_realname}%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.kairo.at/download/mozskins.html
BuildRequires:	unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
This skin reflects the early days of Mozilla (M4 to M8) and tries to restore
the blue-styled look of like those early milestones in current builds
without cutting any functionality.

%description -l pl
Oryginalna skórka Mozilli, u¿ywana przed utworzeniem Modern 1.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post 
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
