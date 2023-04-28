%global octpkg video

Summary:	Video manipulation functions for Octave
Name:		octave-video
Version:	2.0.2
Release:	2
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/video/
Source0:	https://downloads.sourceforge.net/octave/video-%{version}.tar.gz
# (ubuntu)
Patch0:		use-cxxflags.patch
Patch1:		octave-video-fix_ffmpeg5.patch
# (upstream) https://savannah.gnu.org/bugs/index.php?61693
Patch2:		octave-video-2.0.2-allow_FrameRate_to_be_changed.patch
# (upstream) https://savannah.gnu.org/bugs/index.php?61721
Patch3:		octave-video-2.0.2-fix-duration-updates.patch


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
export CC=gcc
export CXX=g++
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
# FIXME disable test dut to octave crashes
#octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

