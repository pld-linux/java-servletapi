Summary:	Servlet API
Summary(pl):	API do servletów
Name:		jakarta-servletapi
Version:	4
Release:	2
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-tomcat-4.0/release/v4.0/src/%{name}-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/tomcat/index.html
Requires:	jdk
BuildRequires:	jakarta-ant
BuildRequires:	jaxp
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
if [ ! `echo $JAVA_HOME` ]; then
	echo "You haven't JAVA_HOME variable set. Can't continue."
	exit 1
fi
PATH="$PATH:$JAVA_HOME/bin"
ANT_HOME="%{_javalibdir}"
export ANT_HOME PATH

ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

gzip -9nf BUILDING.txt LICENSE README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs/*
