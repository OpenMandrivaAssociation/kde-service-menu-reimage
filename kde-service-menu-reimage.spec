Name:           kde-service-menu-reimage
Version:        2.4
Release:        1
Summary:        Simple manipulate on images with their metadata
License:        GPL-3.0
Group:          Productivity/Graphics/Viewers
URL:            https://store.kde.org/p/1231579/
#Source0:        https://store.kde.org/p/1231579/startdownload?file_id=1546539878&file_name=kde-service-menu-reimage-2.4_all.tar.gz&file_type=application/x-gzip&file_size=16880
Source0:        %{name}-%{version}_all.tar.gz

BuildRequires:  imagemagick
BuildRequires:  jhead

Requires: imagemagick
Requires: jhead
Requires: kdialog
Requires: dolphin

%description
kde-service-menu-reimage is a package that extends the functionalities of Dolphin/Konqueror 
adding many additionally sensible menu, reachables with right click on the files. 
It's similar to gnome nautilus actions. These actions are related to picture files.

%prep
%setup -qn %{name}-%{version}_all

%build

%install

install -m 755 bin/* "${bin_dir}"
install -m 644 ServiceMenus/*.desktop "${desktop_dir}"
install -d "${doc_dir}"
install -m 644 doc/* "${doc_dir}"

%files
    
