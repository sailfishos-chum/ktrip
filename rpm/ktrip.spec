%global qt6_version 6.8.3

Name:           ktrip
Version:        25.04.3
Release:        1%{?dist}
License:        GPLv2+
Summary:        Public transport navigation
Url:            https://apps.kde.org/ktrip/
Source:         ktrip-%{version}.tar.xz
Source1:        org.kde.ktrip-86.png
Source2:        org.kde.ktrip-108.png
Source3:        org.kde.ktrip-128.png
Source4:        org.kde.ktrip-256.png

Patch0:        0000-build-for-sailfishos.patch

%global __requires_exclude ^libKPublicTransport.*$

BuildRequires: desktop-file-utils
BuildRequires: kf6-extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-rpm-macros
BuildRequires: kde-kpublictransport-devel
#BuildRequires: qqc2-breeze-style

BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtquickcontrols2-devel

BuildRequires: kf6-kcodecs-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kitemmodels-devel

BuildRequires: pkgconfig(zlib)

Requires: kf6-kconfig-gui
Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: kf6-kcoreaddons
Requires: qt-runner
Requires: kde-kpublictransport

%description
Public transport navigation, allows you to find journeys between specified
locations, departures for a specific station and shows real-time delay and
disruption information.

Title: KTrip
Type: desktop-application
Categories:
  - Maps
  - Utilities
Custom:
  Repo: https://invent.kde.org/utilities/ktrip
  PackagingRepo: https://github.com/sailfishos-chum/ktrip
PackageIcon: https://raw.githubusercontent.com/sailfishos-chum/ktrip/main/rpm/org.kde.ktrip-256.png

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6  \
        -DKDE_INSTALL_BINDIR:PATH=/usr/bin \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr/ \
        -DSAILFISHOS:BOOL=ON \
        %{nil}
%cmake_build

%install
%cmake_install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop

# copy icons
install -p -m644 -D %{SOURCE1} \
    %{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE2} \
    %{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE3} \
    %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE4} \
    %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/org.kde.%{name}.png


%files
%{_bindir}/%{name}
%{_datadir}/locale/
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_kf6_metainfodir}/org.kde.ktrip.appdata.xml
