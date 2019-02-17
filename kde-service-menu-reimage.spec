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
%setup -q

%build

%install

bin_dir="$(kf5-config --path exe | sed "s/.*://")"
    install -d "${pkgdir}${bin_dir}"
    install -m 755 ${source_path}/bin/* "${pkgdir}${bin_dir}"

    desktop_dir="$(kf5-config --path services | sed "s/.*://")ServiceMenus/"
    install -d "${pkgdir}${desktop_dir}"
    install -m 644 ${source_path}/ServiceMenus/*.desktop "${pkgdir}${desktop_dir}"

    doc_dir="$(kf5-config --prefix)/share/doc/kde-service-menu-steghide/"
    install -d "${pkgdir}${doc_dir}"
    install -m 644 ${source_path}/doc/* "${pkgdir}${doc_dir}"
    
    %files
    
