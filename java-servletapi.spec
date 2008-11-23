# TODO:
#	- find some decent replacement. this package is old and
#	obsoleted, but seems good enough as build dependency
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
%include	/usr/lib/rpm/macros.java
Summary:	Java Servlet and JSP API Classes
Summary(pl.UTF-8):	Klasy API z implementacją Java Servlet i JSP
Name:		java-servletapi
Version:	4
Release:	12
License:	Apache
Group:		Libraries/Java
Source0:	http://jakarta.apache.org/builds/jakarta-tomcat-4.0/release/v4.0/src/jakarta-servletapi-%{version}-src.tar.gz
# Source0-md5:	cbf88ed51ee2be5a6ce3bace9d8bdb62
Patch0:		jakarta-servletapi-ant.patch
URL:		http://tomcat.apache.org/
BuildRequires:	ant >= 1.3
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Provides:	jakarta-servletapi
Requires:	jre
Provides:	servlet = 4
Provides:	servletapi4
Obsoletes:	jakarta-servletapi
BuildArch:	noarch
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
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-servletapi-doc

%description javadoc
servletapi documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do servletapi.

%prep
%setup -q -n jakarta-servletapi-%{version}-src
%patch0 -p1

%build
%ant dist %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a dist/lib/servlet.jar $RPM_BUILD_ROOT%{_javadir}/servletapi-%{version}.jar
ln -s servletapi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servlet.jar
ln -s servletapi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servletapi4.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc BUILDING.txt LICENSE README.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
