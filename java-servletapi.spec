# TODO:
#	- find some decent replacement. this package is old and
#	obsoleted, but seems good enough as build dependency
Summary:	Java Servlet and JSP API Classes
Summary(pl.UTF-8):	Klasy API z implementacją Java Servlet i JSP
Name:		jakarta-servletapi
Version:	4
Release:	6
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-tomcat-4.0/release/v4.0/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	cbf88ed51ee2be5a6ce3bace9d8bdb62
URL:		http://tomcat.apache.org/
BuildRequires:	ant >= 1.3
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
Provides:	servlet
Provides:	servlet23
Provides:	servlet4
Provides:	servletapi4
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This subproject contains the compiled code for the implementation
classes of the Java Servlet and JSP APIs (packages javax.servlet,
javax.servlet.http, javax.servlet.jsp, and javax.servlet.jsp.tagext).

%description -l pl.UTF-8
Ten podprojekt zawiera skompilowany kod klas zawierających
implementację standardów API Java Servlet i JSP (pakiety
javax.servlet, javax.servlet.http, javax.servlet.jsp, and
javax.servlet.jsp.tagext).

%package javadoc
Summary:	servletapi documentation
Summary(pl.UTF-8):	Dokumentacja do servletapi
Group:		Development/Languages/Java
Requires:	jpackage-utils
Obsoletes:	jakarta-servletapi-doc

%description javadoc
servletapi documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do servletapi.

%prep
%setup -q -n %{name}-%{version}-src

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%ant dist -Dservletapi.build=build -Dservletapi.dist=dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}
install dist/lib/servlet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servlet.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servletapi4.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUILDING.txt LICENSE README.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
