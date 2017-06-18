%define octpkg video

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Video manipulation functions for Octave
Name:		octave-%{octpkg}
Version:	1.2.3
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	BSD
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.2
BuildRequires:	ffmpeg-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A wrapper for ffmpeg's libavformat and libavcodec, implementing
addframe, avifile, aviinfo and aviread.

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

