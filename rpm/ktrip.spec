Name:           ktrip
Version:        23.04.3
Release:        1%{?dist}
License:        GPLv2+
Summary:        Public transport navigation, allows you to find journeys between specified locations, departures for a specific station and shows real-time delay and disruption information.
Url:            https://apps.kde.org/ktrip/
Source:         ktrip-%{version}.tar.xz
Source1:        org.kde.ktrip-86.png
Source2:        org.kde.ktrip-108.png
Source3:        org.kde.ktrip-128.png
Source4:        org.kde.ktrip-256.png

Patch1:        0001-remove-qq2-desktop-style.patch
Patch2:        0002-desktop-qtrunner.patch

# patches added to upstream to improve functionality or fix bugs
Patch100: git-0001-Use-geo-URI-to-show-location-on-map.patch
Patch101: git-0002-Wait-till-location-query-has-finished-before-making-.patch
Patch102: git-0003-Add-query-delay-to-avoid-calling-service-while-typin.patch


%global __requires_exclude ^libKPublicTransport.*$
%{?opt_kf5_default_filter}

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: opt-kf5-kirigami2-devel
BuildRequires: opt-kf5-kirigami-addons-dateandtime
BuildRequires: opt-kf5-rpm-macros
BuildRequires: opt-kpublictransport-devel
BuildRequires: qqc2-breeze-style

BuildRequires: opt-qt5-qtdeclarative-devel
BuildRequires: opt-qt5-qtquickcontrols2-devel

BuildRequires: opt-kf5-kcodecs-devel
BuildRequires: opt-kf5-kconfig-devel
BuildRequires: opt-kf5-kcoreaddons-devel
BuildRequires: opt-kf5-ki18n-devel
BuildRequires: opt-kf5-kitemmodels-devel

BuildRequires: pkgconfig(zlib)

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-kf5-kconfig-gui
Requires: opt-kf5-kirigami2
Requires: opt-kf5-kirigami-addons
Requires: opt-kf5-kcoreaddons
Requires: qt-runner
Requires: opt-kpublictransport

%description
%{summary}.

PackageName: KTrip
Type: desktop-application
Categories:
  - Maps
  - Utilities
Custom:
  Repo: https://invent.kde.org/utilities/ktrip
  PackagingRepo: https://github.com/sailfishos-chum/ktrip
Icon: https://raw.githubusercontent.com/sailfishos-chum/ktrip/main/rpm/org.kde.ktrip-256.png

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5  \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
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
%{_opt_kf5_metainfodir}/org.kde.ktrip.appdata.xml
