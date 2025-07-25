%global debug_package %{nil}

Name:           kde-service-menu-reimage
Version:        2.6.0
Release:        0.beta.2
Summary:        Simple manipulate on images with their metadata
License:        GPL-3.0
Group:          Productivity/Graphics/Viewers
URL:            https://store.kde.org/p/1231579/
#Source0:        https://store.kde.org/p/1231579/startdownload?file_id=1546539878&file_name=kde-service-menu-reimage-2.4_all.tar.gz&file_type=application/x-gzip&file_size=16880
#Source0:        %{name}-%{version}_all.tar.gz
Source0:        https://github.com/eclipseo/reimage/archive/refs/tags/v2.6.0-beta.2/reimage/reimage-2.6.0-beta.2.tar.gz

BuildRequires:  imagemagick
BuildRequires:  jhead
BuildRequires:	cmake(ECM)

Requires: imagemagick
Requires: jhead
Requires: plasma6-kdialog
Requires: plasma6-dolphin
Requires: libwebp-tools

%description
kde-service-menu-reimage is a package that extends the functionalities of Dolphin/Konqueror 
adding many additionally sensible menu, reachables with right click on the files. 
It's similar to gnome nautilus actions. These actions are related to picture files.

%prep
%autosetup -n reimage-2.6.0-beta.2 -p1

%build

%install
mkdir -p %{buildroot}%_bindir
mkdir -p %{buildroot}/usr/share/kio/servicemenus
mkdir -p %{buildroot}%{_docdir}%{name}

install -m 644 ServiceMenus/*.desktop %{buildroot}/usr/share/kio/servicemenus/
install -m 755 bin/* %{buildroot}%_bindir/
install -m 644 doc/* %{buildroot}%{_docdir}%{name}/

%files
%_bindir/*
%{_datadir}/kio/servicemenus/
%{_docdir}%{name}/
