%define major 5
%define libname %mklibname KPimKDav2 %{major}
%define devname %mklibname KPimKDav2 -d
# Doesn't follow usual versioning schemes yet -- always unstable for now
%define stable unstable

Name:		kdav2
Version:	0.2.0
Release:	1
Source0:	http://download.kde.org/%{stable}/kdav2/%{version}/src/%{name}-%{version}.tar.xz
Summary:	KDE library for accessing data over DAV
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5XmlPatterns)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5CoreAddons)

%description
KDE library for accessing data over DAV

%package -n %{libname}
Summary: KDE library for accessing data over DAV
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for accessing data over DAV

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/kdav2.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.0*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri