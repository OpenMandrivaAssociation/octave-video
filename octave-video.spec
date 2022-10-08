%global octpkg video

Summary:	Video manipulation functions for Octave
Name:		octave-%{octpkg}
Version:	2.0.2
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	BSD
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
# (ubuntu)
Patch0:		use-cxxflags.patch
Patch1:		octave-video-fix_ffmpeg5.patch

BuildRequires:	octave-devel >= 4.4.0
BuildRequires:	ffmpeg-devel
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A wrapper for ffmpeg's libavformat and libavcodec, implementing
addframe, avifile, aviinfo and aviread.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
export CC=gcc
export CXX=g++
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

