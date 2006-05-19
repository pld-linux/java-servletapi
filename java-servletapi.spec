Summary:	Java Servlet and JSP API Classes
Summary(pl):	Klasy API z implementacj± Java Servlet i JSP
Name:		jakarta-servletapi
Version:	4
Release:	4
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-tomcat-4.0/release/v4.0/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	cbf88ed51ee2be5a6ce3bace9d8bdb62
URL:		http://jakarta.apache.org/tomcat/index.html
BuildRequires:	ant >= 1.3
Requires:	jre
Provides:	servlet
Provides:	servlet4
Provides:	servlet23
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
This subproject contains the compiled code for the implementation
classes of the Java Servlet and JSP APIs (packages javax.servlet,
javax.servlet.http, javax.servlet.jsp, and javax.servlet.jsp.tagext).

%description -l pl
Ten podprojekt zawiera skompilowany kod klas zawieraj±cych
implementacjê standardów API Java Servlet i JSP (pakiety
javax.servlet, javax.servlet.http, javax.servlet.jsp, and
javax.servlet.jsp.tagext).

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
ant dist -Dservletapi.build=build -Dservletapi.dist=dist

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
