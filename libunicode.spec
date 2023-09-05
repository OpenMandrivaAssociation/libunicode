%define major 0
%define libname %mklibname unicode
%define devname %mklibname unicode -d

Name: libunicode
Version: 0.3.0
Release: 1
Source0: https://github.com/contour-terminal/libunicode/archive/refs/tags/v%{version}.tar.gz
Patch0: https://src.fedoraproject.org/rpms/libunicode/raw/rawhide/f/fix-ucd.patch
Summary: Modern C++17 Unicode Library
URL: https://github.com/contour-terminal/libunicode
License: Apache-2.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(Catch2)
BuildRequires: pkgconfig(fmt)
BuildRequires: range-v3-devel
BuildRequires: unicode-ucd

%description
Modern C++17 Unicode Library
The goal of this library is to bring painless unicode support to C++ with
simple and easy to understand APIs.

The API naming conventions are chosen to look familiar to those using the C++
standard libary.

Feature Overview
 API for accessing UCD properties
 UTF8 <-> UTF32 conversion
 wcwidth equivalent (int unicode::width(char32_t))
 grapheme segmentation (UTS algorithm)
 symbol/emoji segmentation (UTS algorithm)
 script segmentation UTS 24
 unit tests for most parts (wcwidth / segmentation)
 generic text run segmentation (top level segmentation API suitable for text
  shaping implementations)
 word segmentation (UTS algorithm)
 CLI tool: uc-inspect for inspecting input files by code point properties,
  grapheme cluster, word, script, ...

%package -n %{libname}
Summary: Modern C++17 Unicode Library
Group: System/Libraries

%description -n %{libname}
Modern C++17 Unicode Library
The goal of this library is to bring painless unicode support to C++ with
simple and easy to understand APIs.

The API naming conventions are chosen to look familiar to those using the C++
standard libary.

Feature Overview
 API for accessing UCD properties
 UTF8 <-> UTF32 conversion
 wcwidth equivalent (int unicode::width(char32_t))
 grapheme segmentation (UTS algorithm)
 symbol/emoji segmentation (UTS algorithm)
 script segmentation UTS 24
 unit tests for most parts (wcwidth / segmentation)
 generic text run segmentation (top level segmentation API suitable for text
  shaping implementations)
 word segmentation (UTS algorithm)
 CLI tool: uc-inspect for inspecting input files by code point properties,
  grapheme cluster, word, script, ...

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Modern C++17 Unicode Library
The goal of this library is to bring painless unicode support to C++ with
simple and easy to understand APIs.

The API naming conventions are chosen to look familiar to those using the C++
standard libary.

Feature Overview
 API for accessing UCD properties
 UTF8 <-> UTF32 conversion
 wcwidth equivalent (int unicode::width(char32_t))
 grapheme segmentation (UTS algorithm)
 symbol/emoji segmentation (UTS algorithm)
 script segmentation UTS 24
 unit tests for most parts (wcwidth / segmentation)
 generic text run segmentation (top level segmentation API suitable for text
  shaping implementations)
 word segmentation (UTS algorithm)
 CLI tool: uc-inspect for inspecting input files by code point properties,
  grapheme cluster, word, script, ...

%prep
%autosetup -p1

# Adapt to newer catch2
find . -name "*.cpp" -o -name "*.h" |xargs sed -i -e 's,catch2/catch.hpp,catch2/catch_all.hpp,'

%cmake \
	-DLIBUNICODE_UCD_DIR=%{_datadir}/unicode/ucd \
	-G Ninja

%build
export LD_LIBRARY_PATH=$(pwd)/build/src/libunicode
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
