Name:           ktrip
Version:        23.03.90
Release:        1%{?dist}
License:        GPLv2+
Summary:        Public transport navigation, allows you to find journeys between specified locations, departures for a specific station and shows real-time delay and disruption information.
Url:            https://apps.kde.org/ktrip/
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/ktrip-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-kirigami2-addons-dateandtime
BuildRequires: kf5-rpm-macros
BuildRequires: kpublictransport-devel
BuildRequires: qqc2-desktop-style
BuildRequires: reuse

BuildRequires: opt-qt5-qtcore-devel
BuildRequires: opt-qt5-qtdeclarateive-devel
BuildRequires: opt-qt5-qtquickcontrols2-devel

BuildRequires: opt-kf5-kcodecs-devel
BuildRequires: opt-kf5-kconfig-devel
BuildRequires: opt-kf5-kcoreaddons-devel
BuildRequires: opt-kf5-ki18n-devel
BuildRequires: opt-kf5-kitemmodels-devel

BuildRequires: pkgconfig(zlib)

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%opt_cmake_kf5
%make_build

%install
%make_install -C build
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_kf5_datadir}/applications/ %{buildroot}/%{_kf5_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%{_opt_kf5_bindir}/%{name}

%{_opt_kf5_datadir}/applications/org.kde.%{name}.desktop
%{_opt_kf5_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*

%{_opt_kf5_metainfodir}/org.kde.%{name}.appdata.xml