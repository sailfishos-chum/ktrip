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

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%make_build
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%{_opt_kf5_bindir}/%{name}

%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
