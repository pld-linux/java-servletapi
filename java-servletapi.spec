# NOTE: it's an old servletapi version; see java-servletapi5.spec or tomcat.spec for more recent
# TODO: rename to java-servletapi4?
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
Summary:	Java Servlet 2.3 and JSP 1.2 API Classes
Summary(pl.UTF-8):	Klasy API z implementacją Java Servlet 2.3 i JSP 1.2
Name:		java-servletapi
Version:	4
Release:	12
License:	Apache v1.1
Group:		Libraries/Java
Source0:	http://jakarta.apache.org/builds/jakarta-tomcat-4.0/release/v4.0/src/jakarta-servletapi-%{version}-src.tar.gz
# Source0-md5:	cbf88ed51ee2be5a6ce3bace9d8bdb62
Patch0:		jakarta-servletapi-ant.patch
URL:		http://tomcat.apache.org/
BuildRequires:	ant >= 1.3
BuildRequires:	jdk >= 1.3
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre >= 1.3
Provides:	java(jsp) = 1.2
Provides:	java(servlet) = 2.3
Obsoletes:	jakarta-servletapi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This subproject contains the compiled code for the implementation
classes of the Java Servlet 2.3 and JSP 1.2 APIs (packages
javax.servlet, javax.servlet.http, javax.servlet.jsp, and
javax.servlet.jsp.tagext).

%description -l pl.UTF-8
Ten podprojekt zawiera skompilowany kod klas zawierających
implementację standardów API Java Servlet 2.3 i JSP 1.2 (pakiety
javax.servlet, javax.servlet.http, javax.servlet.jsp, and
javax.servlet.jsp.tagext).

%package javadoc
Summary:	servletapi 4 documentation
Summary(pl.UTF-8):	Dokumentacja do servletapi 4
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-servletapi-doc

%description javadoc
servletapi 4 documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do servletapi 4.

%prep
%setup -q -n jakarta-servletapi-%{version}-src
%patch0 -p1

%build
%ant dist %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a dist/lib/servlet.jar $RPM_BUILD_ROOT%{_javadir}/servlet-%{version}.jar
ln -s servlet-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servlet-api-2.3.jar
ln -s servlet-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servlet-api.jar
ln -s servlet-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jsp-api-1.2.jar
ln -s servlet-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jsp-api.jar

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
%doc LICENSE README.txt
%{_javadir}/servlet-%{version}.jar
%{_javadir}/servlet-api-2.3.jar
%{_javadir}/servlet-api.jar
%{_javadir}/jsp-api-1.2.jar
%{_javadir}/jsp-api.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
