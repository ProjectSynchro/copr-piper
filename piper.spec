%global commit 40880d2979174c46f5342ee8742ac1e70cc8d62c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20240617T121819Z
%global tag v0.8.2
%global clean_tag %(echo %{tag} | sed 's/^v//')

%define debug_package %{nil}

Name:           oversteer
Version:        %{clean_tag}^%{git_date}.g%{shortcommit}
Release:        %autorelease
Summary:        GTK application to configure gaming mice
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/libratbag/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

BuildArch: noarch

BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: python3-cairo
BuildRequires: python3-devel
BuildRequires: python3-evdev
BuildRequires: python3-flake8
BuildRequires: python3-gobject
BuildRequires: python3-lxml

BuildRequires: appstream
BuildRequires: desktop-file-utils
BuildRequires: gettext-devel
BuildRequires: git-core
BuildRequires: libappstream-glib
BuildRequires: libratbag-ratbagd
BuildRequires: meson

Requires: gtk3
Requires: hicolor-icon-theme
Requires: libratbag-ratbagd >= 0.14
Requires: python3-cairo
Requires: python3-evdev
Requires: python3-gobject
Requires: python3-lxml

%description
Piper is a GTK+ application to configure gaming mice, using libratbag
via ratbagd.

%prep
%autosetup -p1 -N -n %{name}-%{commit}

%build
%meson -Dpython="%{python3}"

%meson_build

%check
%meson_test
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%pycached %{python3_sitelib}/%{name}/*.py
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*.1*

%changelog
%autochangelog
