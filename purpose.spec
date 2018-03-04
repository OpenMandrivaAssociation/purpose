Name:		purpose
Version:	5.44.0
Release:        1
Summary:        Provides abstractions to get the developer's purposes fulfilled
License:        LGPL-2.1+
Group:          System/Base
Url:            http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:        http://download.kde.org/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
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
BuildRequires:	kdeconnect

%description
Framework for providing abstractions to get the developer's purposes fulfilled.

%files -f %{name}.lang
%{_kde5_datadir}/purpose
%{_kde5_qmldir}/org/kde/%{name}
%{_kde5_iconsdir}/*/*/*/*
%{_libdir}/libexec/kf5/purposeprocess
%{_datadir}/accounts/services/kde/*.service
%{_datadir}/kpackage/Purpose/Twitter
%dir %{_libdir}/qt5/plugins/kf5/purpose
%{_libdir}/qt5/plugins/kf5/purpose/emailplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/imgurplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/kdeconnectplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/ktpsendfileplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/nextcloudplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/pastebinplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/phabricatorplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/reviewboardplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/saveasplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/youtubeplugin.so


#--------------------------------------------------------------------

%define major 5
%define libname %mklibname KF5Purpose %{major}

%package -n %{libname}
Summary:	Provides abstractions to get the developer's purposes fulfilled
Group:		System/Libraries
Obsoletes:	%{mklibname kf5purpose 5} < %{EVRD}
Provides:	%{mklibname kf5purpose 5} = %{EVRD}

%description -n %{libname}
Provides abstractions to get the developer's purposes fulfilled.

%files -n %{libname}
%_kde5_libdir/libKF5Purpose.so.%{major}
%_kde5_libdir/libKF5Purpose.so.%{major}.*

%libpackage PhabricatorHelpers %{major}

%libpackage ReviewboardHelpers %{major}

#--------------------------------------------------------------------

%define purposewidgets_major 5
%define libpurposewidgets %mklibname KF5PurposeWidgets %{purposewidgets_major}

%package -n %{libpurposewidgets}
Summary:        Provides abstractions to get the developer's purposes fulfilled
Group:          System/Libraries
Obsoletes:	%{mklibname kf5purposewidgets 5} < %{EVRD}
Provides:	%{mklibname kf5purposewidgets 5} = %{EVRD}

%description -n %{libpurposewidgets}
Provides abstractions to get the developer's purposes fulfilled.

%files -n %{libpurposewidgets}
%_kde5_libdir/libKF5PurposeWidgets.so.%{purposewidgets_major}
%_kde5_libdir/libKF5PurposeWidgets.so.%{purposewidgets_major}.*

#--------------------------------------------------------------------

%package devel
Summary:        Provides abstractions to get the developer's purposes fulfilled
Group:          Development/KDE and Qt
Requires:       %{libname} = %{EVRD}
Requires:	%{libpurposewidgets} = %{EVRD}

%description devel
Framework for providing abstractions to get the developer's purposes fulfilled.
Development files.

%files devel
%{_kde5_libdir}/libKF5Purpose.so
%{_kde5_libdir}/libKF5PurposeWidgets.so
%{_kde5_libdir}/cmake/KDEExperimentalPurpose/
%{_libdir}/cmake/KF5Purpose
%{_kde5_includedir}/*
%{_sysconfdir}/xdg/purpose.categories

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libpurpose_quick
%find_lang libpurpose_widgets

for i in imgur email ktp-sendfile nextcloud pastebin reviewboard saveas youtube; do
  %find_lang purpose_$i
done

cat *.lang > %{name}.lang
