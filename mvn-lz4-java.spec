#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-lz4-java
Version  : 1.4.0
Release  : 4
URL      : https://github.com/lz4/lz4-java/archive/1.4.0.tar.gz
Source0  : https://github.com/lz4/lz4-java/archive/1.4.0.tar.gz
Source1  : https://repo1.maven.org/maven2/net/jpountz/lz4/lz4/1.2.0/lz4-1.2.0.jar
Source2  : https://repo1.maven.org/maven2/net/jpountz/lz4/lz4/1.2.0/lz4-1.2.0.pom
Source3  : https://repo1.maven.org/maven2/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.jar
Source4  : https://repo1.maven.org/maven2/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom
Source5  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.jar
Source6  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.pom
Source7  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.4.1/lz4-java-1.4.1.jar
Source8  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.4.1/lz4-java-1.4.1.pom
Source9  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.6.0/lz4-java-1.6.0.jar
Source10  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.6.0/lz4-java-1.6.0.pom
Summary  : fast lossless compression algorithm library
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause GPL-2.0
Requires: mvn-lz4-java-data = %{version}-%{release}
Requires: mvn-lz4-java-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-cmake
BuildRequires : buildreq-mvn

%description
# LZ4 Java
LZ4 compression for Java, based on Yann Collet's work available at
http://code.google.com/p/lz4/.

%package data
Summary: data components for the mvn-lz4-java package.
Group: Data

%description data
data components for the mvn-lz4-java package.


%package license
Summary: license components for the mvn-lz4-java package.
Group: Default

%description license
license components for the mvn-lz4-java package.


%prep
%setup -q -n lz4-java-1.4.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-lz4-java
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-lz4-java/LICENSE.txt
cp src/lz4/LICENSE %{buildroot}/usr/share/package-licenses/mvn-lz4-java/src_lz4_LICENSE
cp src/lz4/programs/COPYING %{buildroot}/usr/share/package-licenses/mvn-lz4-java/src_lz4_programs_COPYING
cp src/xxhash/LICENSE %{buildroot}/usr/share/package-licenses/mvn-lz4-java/src_xxhash_LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.2.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.2.0/lz4-1.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.2.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.2.0/lz4-1.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.3.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.3.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.1/lz4-java-1.4.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.1/lz4-java-1.4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.6.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.6.0/lz4-java-1.6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.6.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.6.0/lz4-java-1.6.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.2.0/lz4-1.2.0.jar
/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.2.0/lz4-1.2.0.pom
/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.jar
/usr/share/java/.m2/repository/net/jpountz/lz4/lz4/1.3.0/lz4-1.3.0.pom
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.jar
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.pom
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.1/lz4-java-1.4.1.jar
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.1/lz4-java-1.4.1.pom
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.6.0/lz4-java-1.6.0.jar
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.6.0/lz4-java-1.6.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-lz4-java/LICENSE.txt
/usr/share/package-licenses/mvn-lz4-java/src_lz4_LICENSE
/usr/share/package-licenses/mvn-lz4-java/src_lz4_programs_COPYING
/usr/share/package-licenses/mvn-lz4-java/src_xxhash_LICENSE
