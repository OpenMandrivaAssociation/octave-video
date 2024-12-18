%global octpkg video

Summary:	Video manipulation functions for Octave
Name:		octave-video
Version:	2.1.1
Release:	5
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/video/
#Source0:	https://downloads.sourceforge.net/octave/video-%{version}.tar.gz
Source0:	https://github.com/Andy1978/octave-video/releases/download/%{version}/video-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:	ffmpeg-devel
BuildRequires:	gomp-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A wrapper for ffmpeg's libavformat and libavcodec, implementing
addframe, avifile, aviinfo and aviread.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
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

