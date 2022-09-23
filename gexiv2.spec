#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gexiv2
Version  : 0.14.0
Release  : 26
URL      : https://download.gnome.org/sources/gexiv2/0.14/gexiv2-0.14.0.tar.xz
Source0  : https://download.gnome.org/sources/gexiv2/0.14/gexiv2-0.14.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gexiv2-data = %{version}-%{release}
Requires: gexiv2-lib = %{version}-%{release}
Requires: gexiv2-license = %{version}-%{release}
Requires: gexiv2-python = %{version}-%{release}
Requires: gexiv2-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : exiv2-dev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(exiv2)
BuildRequires : pygobject
BuildRequires : vala
BuildRequires : vala-dev

%description
gexiv2 - A GObject-based Exiv2 wrapper
--------------------------------------
* Introduction

%package data
Summary: data components for the gexiv2 package.
Group: Data

%description data
data components for the gexiv2 package.


%package dev
Summary: dev components for the gexiv2 package.
Group: Development
Requires: gexiv2-lib = %{version}-%{release}
Requires: gexiv2-data = %{version}-%{release}
Provides: gexiv2-devel = %{version}-%{release}
Requires: gexiv2 = %{version}-%{release}

%description dev
dev components for the gexiv2 package.


%package lib
Summary: lib components for the gexiv2 package.
Group: Libraries
Requires: gexiv2-data = %{version}-%{release}
Requires: gexiv2-license = %{version}-%{release}

%description lib
lib components for the gexiv2 package.


%package license
Summary: license components for the gexiv2 package.
Group: Default

%description license
license components for the gexiv2 package.


%package python
Summary: python components for the gexiv2 package.
Group: Default
Requires: gexiv2-python3 = %{version}-%{release}

%description python
python components for the gexiv2 package.


%package python3
Summary: python3 components for the gexiv2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the gexiv2 package.


%prep
%setup -q -n gexiv2-0.14.0
cd %{_builddir}/gexiv2-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635730395
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dpython3_girdir=true  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gexiv2
cp %{_builddir}/gexiv2-0.14.0/COPYING %{buildroot}/usr/share/package-licenses/gexiv2/be0b40ce8f9532b75966a20d14af123d3c6b05aa
cp %{_builddir}/gexiv2-0.14.0/debian/copyright %{buildroot}/usr/share/package-licenses/gexiv2/93aa7c82f62a2b22955f87e9eb752b74d33c68f1
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/true/GExiv2.py

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GExiv2-0.10.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gexiv2.deps
/usr/share/vala/vapi/gexiv2.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gexiv2/gexiv2-enums.h
/usr/include/gexiv2/gexiv2-log.h
/usr/include/gexiv2/gexiv2-managed-stream.h
/usr/include/gexiv2/gexiv2-metadata.h
/usr/include/gexiv2/gexiv2-preview-image.h
/usr/include/gexiv2/gexiv2-preview-properties.h
/usr/include/gexiv2/gexiv2-startup.h
/usr/include/gexiv2/gexiv2-version.h
/usr/include/gexiv2/gexiv2.h
/usr/lib64/libgexiv2.so
/usr/lib64/pkgconfig/gexiv2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgexiv2.so.2
/usr/lib64/libgexiv2.so.2.14.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gexiv2/93aa7c82f62a2b22955f87e9eb752b74d33c68f1
/usr/share/package-licenses/gexiv2/be0b40ce8f9532b75966a20d14af123d3c6b05aa

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
