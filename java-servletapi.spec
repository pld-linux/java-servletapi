Summary:	Servlet API
Summary(pl):	API do servletów
Name:		jakarta-servletapi
Version:	4
Release:	3
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-tomcat-4.0/release/v4.0/src/%{name}-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/tomcat/index.html
BuildRequires:	jakarta-ant >= 1.3
BuildRequires:	jaxp >= 1.1
Requires:	jaxp >= 1.1
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Servlet API.

%description -l pl
API do servletów.

%package doc
Summary:	servletapi documentation
Summary(pl):	Dokumentacja do servletapi
Group:		Development/Languages/Java

%description doc
servletapi documentation.

%description doc -l pl
Dokumentacja do servletapi.

%prep
%setup -q -n %{name}-%{version}-src

%build
if [ -z "$JAVA_HOME" ]; then
	JAVA_HOME=/usr/lib/java
fi
ANT_HOME="%{_javalibdir}"
export JAVA_HOME ANT_HOME

ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUILDING.txt LICENSE README.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs/*
