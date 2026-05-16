#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%{?use_default_jdk:%use_default_jdk 8}

Summary:	Java Servlet 4.0 API
Summary(pl.UTF-8):	API Java Servlet 4.0
Name:		java-servletapi
Version:	4.0.1
Release:	2
License:	CDDL v1.1 or GPL v2 with Classpath exception
Group:		Libraries/Java
#Source0Download: https://github.com/javaee/servlet-spec/releases
Source0:	https://github.com/javaee/servlet-spec/archive/refs/tags/%{version}/servlet-spec-%{version}.tar.gz
# Source0-md5:	bfb6f2ce27bdcca12159b48e1db9bf7a
URL:		https://javaee.github.io/servlet-spec/
%buildrequires_jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 2.058
Provides:	java(servlet) = 4.0
Obsoletes:	jakarta-servletapi
Obsoletes:	java-servletapi5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java Servlet 4.0 API classes (packages javax.servlet,
javax.servlet.http, javax.servlet.descriptor, javax.servlet.annotation).

%description -l pl.UTF-8
Klasy API Java Servlet 4.0 (pakiety javax.servlet, javax.servlet.http,
javax.servlet.descriptor, javax.servlet.annotation).

%package javadoc
Summary:	Java Servlet API documentation
Summary(pl.UTF-8):	Dokumentacja API Java Servlet
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-servletapi-doc

%description javadoc
Java Servlet API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API Java Servlet.

%prep
%setup -q -n servlet-spec-%{version}

%build
export JAVA_HOME="%{java_home}"

install -d target/classes
%javac -d target/classes \
	-source 1.8 -target 1.8 \
	-encoding UTF-8 \
	$(find src/main/java -name '*.java')

# LocalStrings.properties (alongside .java sources, per pom.xml resources)
# is loaded by GenericFilter at runtime; %javac doesn't copy non-.java files.
cd src/main/java
find . -name '*.properties' -exec cp --parents '{}' ../../../target/classes/ \;
cd ../../..
test -s target/classes/javax/servlet/LocalStrings.properties

cd target/classes
%jar cf ../servlet-api-%{version}.jar javax
cd ../..

%if %{with javadoc}
%javadoc -d target/apidocs \
	-source 1.8 \
	-encoding UTF-8 \
	-Xdoclint:none \
	-subpackages javax.servlet \
	-sourcepath src/main/java
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install target/servlet-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servlet-api-%{version}.jar
ln -sf servlet-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/servlet-api.jar

%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a target/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_javadir}/servlet-api-%{version}.jar
%{_javadir}/servlet-api.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
