Summary: 	servletapi
Summary(pl):	servletapi
Name:		jakarta-servletapi
Version:	4
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	http://jakarta.apache.org/dist/jakarta/jakarta-tomcat-4.0/release/v4.0/src/%{name}-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/tomcat/index.html
Requires:	ibm-java-sdk
BuildRequires:	jakarta-ant
BuildRequires:	jaxp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
servletapi

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary: 	servletapi documentation

%description doc
servletapi documentation

%prep
%setup -q -n %{name}-%{version}-src

%build
export JAVA_HOME="/usr/lib/IBMJava2-13"
export ANT_HOME="%{_javalibdir}"

ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp dist/lib/*.jar $RPM_BUILD_ROOT/%{_javalibdir}

gzip -9nf BUILDING.txt LICENSE README.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644 root root 755)
%doc dist/docs/*
