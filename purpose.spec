# Some purpose plugins require kaccounts
%bcond_with bootstrap

Name:		purpose
Version:	5.87.0
Release:	1
Summary:	Provides abstractions to get the developer's purposes fulfilled
License:	LGPL-2.1+
Group:		System/Base
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
%if ! %{with bootstrap}
BuildRequires:	cmake(KAccounts)
BuildRequires:	pkgconfig(libaccounts-glib)
%endif
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	pkgconfig(Qt5Core) >= 5.2
BuildRequires:	pkgconfig(Qt5Qml) >= 5.2
BuildRequires:	pkgconfig(Qt5Gui) >= 5.2
BuildRequires:	pkgconfig(Qt5Test) >= 5.2
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	cmake(ECM)
BuildRequires:	intltool
BuildRequires:	kdeconnect
Requires:	ubuntuonlineaccounts-qml
Requires:	kdeclarative

%description
Framework for providing abstractions to get the developer's purposes fulfilled.

%files -f %{name}.lang
%{_kde5_datadir}/purpose
%{_kde5_qmldir}/org/kde/%{name}
%{_kde5_iconsdir}/*/*/*/*
%{_libdir}/libexec/kf5/purposeprocess
%if ! %{with bootstrap}
%{_datadir}/accounts/services/kde/*.service
%endif
%dir %{_libdir}/qt5/plugins/kf5/kfileitemaction
%{_libdir}/qt5/plugins/kf5/kfileitemaction/sharefileitemaction.so
%dir %{_libdir}/qt5/plugins/kf5/purpose
%{_libdir}/qt5/plugins/kf5/purpose/barcodeplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/bluetoothplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/emailplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/imgurplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/kdeconnectplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/kdeconnectsmsplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/ktpsendfileplugin.so
%if ! %{with bootstrap}
%{_libdir}/qt5/plugins/kf5/purpose/nextcloudplugin.so
%endif
%{_libdir}/qt5/plugins/kf5/purpose/pastebinplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/phabricatorplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/reviewboardplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/saveasplugin.so
%{_libdir}/qt5/plugins/kf5/purpose/telegramplugin.so
%if ! %{with bootstrap}
%{_libdir}/qt5/plugins/kf5/purpose/youtubeplugin.so
%endif

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
%{_kde5_libdir}/libKF5Purpose.so.%{major}
%{_kde5_libdir}/libKF5Purpose.so.%{major}.*

%libpackage PhabricatorHelpers %{major}

%libpackage ReviewboardHelpers %{major}

#--------------------------------------------------------------------

%define purposewidgets_major 5
%define libpurposewidgets %mklibname KF5PurposeWidgets %{purposewidgets_major}

%package -n %{libpurposewidgets}
Summary:	Provides abstractions to get the developer's purposes fulfilled
Group:		System/Libraries
Obsoletes:	%{mklibname kf5purposewidgets 5} < %{EVRD}
Provides:	%{mklibname kf5purposewidgets 5} = %{EVRD}
Conflicts:	%{_lib}kf5purposewidgets5 < %{EVRD}

%description -n %{libpurposewidgets}
Provides abstractions to get the developer's purposes fulfilled.

%files -n %{libpurposewidgets}
%{_kde5_libdir}/libKF5PurposeWidgets.so.%{purposewidgets_major}
%{_kde5_libdir}/libKF5PurposeWidgets.so.%{purposewidgets_major}.*

#--------------------------------------------------------------------

%package devel
Summary:	Provides abstractions to get the developer's purposes fulfilled
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
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
%{_datadir}/qlogging-categories5/purpose.*categories

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libpurpose_quick
%find_lang libpurpose_widgets

for i in barcode bluetooth imgur email kdeconnectsms ktp-sendfile nextcloud pastebin reviewboard saveas youtube kdeconnect phabricator; do
  %find_lang purpose_$i
done
%find_lang purpose-fileitemaction

cat *.lang > %{name}.lang
