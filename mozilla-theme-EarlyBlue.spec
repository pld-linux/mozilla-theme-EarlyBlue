Summary:	The original mozilla skin, used defore the creation of the Modern 1
Summary(pl):	Oryginalna skórka Mozilli, u¿ywana przed utworzeniem Modern 1
Name:		mozilla-theme-EarlyBlue
%define		_realname	EarlyBlue
Version:	1.3
%define	fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.hirsch.sth.ac.at/~robert/kairo.at/dl/%{_realname}%{fver}.xpi
# Source0-md5:	dd1a87c506568fc9dfff17a23ea3bf50
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.kairo.at/download/mozskins.html
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
