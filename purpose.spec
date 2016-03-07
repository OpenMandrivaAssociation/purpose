Name:		purpose
Version:	1.0
Release:        3
Summary:        Provides abstractions to get the developer's purposes fulfilled
License:        LGPL-2.1+
Group:          System/Base
Url:            http://www.kde.org
Source:         http://download.kde.org/stable/purpose/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KAccounts)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	pkgconfig(Qt5Core) >= 5.2
BuildRequires:	pkgconfig(Qt5Qml) >= 5.2
BuildRequires:	pkgconfig(Qt5Gui) >= 5.2
BuildRequires:	pkgconfig(Qt5Test) >= 5.2
BuildRequires:	cmake(ECM)
BuildRequires:	intltool

%description
Framework for providing abstractions to get the developer's purposes fulfilled.

%files
%{_kde5_libdir}/libReviewboardHelpers.so
%{_kde5_datadir}/purpose
%{_qt5_plugindir}/%{name}
%{_kde5_qmldir}/org/kde/%{name}
%{_kde5_iconsdir}/*/*/*/*
%{_kde5_datadir}/accounts/services/google-youtube.service

#--------------------------------------------------------------------

%define purpose_major 5
%define libpurpose %mklibname kf5purpose %{purpose_major}

%package -n %libpurpose
Summary:	Provides abstractions to get the developer's purposes fulfilled
Group:		System/Libraries

%description -n %libpurpose
Provides abstractions to get the developer's purposes fulfilled.

%files -n %libpurpose
%_kde5_libdir/libKF5Purpose.so.%{purpose_major}
%_kde5_libdir/libKF5Purpose.so.%{purpose_major}.*

#--------------------------------------------------------------------

%define purposewidgets_major 5
%define libpurposewidgets %mklibname kf5purposewidgets %{purposewidgets_major}

%package -n %libpurposewidgets
Summary:        Provides abstractions to get the developer's purposes fulfilled
Group:          System/Libraries

%description -n %libpurposewidgets
Provides abstractions to get the developer's purposes fulfilled.

%files -n %libpurposewidgets
%_kde5_libdir/libKF5PurposeWidgets.so.%{purposewidgets_major}
%_kde5_libdir/libKF5PurposeWidgets.so.%{purposewidgets_major}.*

#--------------------------------------------------------------------

%package devel
Summary:        Provides abstractions to get the developer's purposes fulfilled
Group:          Development/KDE and Qt
Requires:       %{libpurpose} = %{version}
Requires:	%{libpurposewidgets} = %{version}

%description devel
Framework for providing abstractions to get the developer's purposes fulfilled.
Development files.

%files devel
%{_kde5_libdir}/libKF5Purpose.so
%{_kde5_libdir}/libKF5PurposeWidgets.so
%{_kde5_libdir}/cmake/KDEExperimentalPurpose/
%{_kde5_includedir}/*

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

