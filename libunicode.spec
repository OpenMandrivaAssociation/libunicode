%define major 0
%define libname %mklibname unicode %{major}

Summary: Unicode library
Name: libunicode
Version: 0.4.gnome
Release: %mkrel 11
License: LGPL
Group: System/Libraries
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 0.4.gnome-3mdk don't add -I/usr/include and -L/usr/lib to CFLAGS/LDFLAGS
Patch0:  libunicode-0.4.gnome-fixinclude.patch
Url: http://www.pango.org/download/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires:	automake1.4

%description
A library to handle unicode strings

%package -n %{libname}
Summary: %{summary}
Group: %{group}
Provides: %{name}
Obsoletes: %{name}

%description -n %{libname}
A library to handle unicode strings

%package -n %{libname}-devel
Summary: A unicode manipulation library
Group: Development/Other
Provides: %{name}-devel = %{name}-%{release}
Obsoletes: %{name}-devel
Requires: %{libname} = %{version}

%description -n %{libname}-devel
This package package includes the static libraries and header files
for the libunicode package.

%prep
%setup -q -n %{name}-0.4
%patch0 -p1 -b .fixflags

# (tv) fix build:
rm -f ltmain.sh
libtoolize -c -f 
#needed by patch0
rm -f configure
aclocal-1.4
autoconf

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog TODO
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/*a
%{_libdir}/*.sh
%{_includedir}/*

