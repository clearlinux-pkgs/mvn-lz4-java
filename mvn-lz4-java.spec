#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-lz4-java
Version  : 1.4.0
Release  : 1
URL      : https://github.com/lz4/lz4-java/archive/1.4.0.tar.gz
Source0  : https://github.com/lz4/lz4-java/archive/1.4.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.jar
Source2  : https://repo1.maven.org/maven2/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.pom
Summary  : fast lossless compression algorithm library
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause GPL-2.0
Requires: mvn-lz4-java-data = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
# LZ4 Java
LZ4 compression for Java, based on Yann Collet's work available at
http://code.google.com/p/lz4/.

%package data
Summary: data components for the mvn-lz4-java package.
Group: Data

%description data
data components for the mvn-lz4-java package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.jar
/usr/share/java/.m2/repository/org/lz4/lz4-java/1.4.0/lz4-java-1.4.0.pom