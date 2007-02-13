Summary:	The original mozilla skin, used defore the creation of the Modern 1
Summary(pl.UTF-8):	Oryginalna skórka Mozilli, używana przed utworzeniem Modern 1
Name:		mozilla-theme-EarlyBlue
%define		_realname	EarlyBlue
Version:	1.7
%define	fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/1_7/%{_realname}%{fver}.xpi
# Source0-md5:	665ae73146946a5f9186c09c57492f54
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.kairo.at/download/mozskins.html
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 5:1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
This skin reflects the early days of Mozilla (M4 to M8) and tries to restore
the blue-styled look of like those early milestones in current builds
without cutting any functionality.

%description -l pl.UTF-8
Ta skórka pokazuje wczesne dni Mozilli (M4 do M8) i próbuje odtworzyć
stylizowany na niebiesko wygląd tych "kamieni milowych" w aktualnych
wydaniach, bez usuwania żadnej funkcjonalności.
Oryginalna skórka Mozilli, używana przed utworzeniem Modern 1.

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
