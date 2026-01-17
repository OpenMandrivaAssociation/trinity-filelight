%bcond clang 1
%bcond gamin 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg filelight
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		1.0
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		Graphical disk usage display
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/utilities/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL="ON"
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# ACL support
BuildRequires:  pkgconfig(libacl)

# ATTR support
BuildRequires:  pkgconfig(libattr)


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes:	filelight-l10n < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	filelight-l10n = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Filelight creates a complex, but data-rich graphical representation of the files and
directories on your computer. 


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/bin/filelight
%{tde_prefix}/share/applications/tde/filelight.desktop
%{tde_prefix}/share/apps/filelight/
%{tde_prefix}/share/icons/crystalsvg/*/actions/view_filelight.png
%{tde_prefix}/share/icons/hicolor/*/apps/filelight.png
%config(noreplace) %{_sysconfdir}/trinity/filelightrc
%{tde_prefix}/share/services/*.desktop
%{tde_prefix}/%{_lib}/trinity/libfilelight.so
%{tde_prefix}/%{_lib}/trinity/libfilelight.la
%lang(da) %{tde_prefix}/share/doc/tde/HTML/da/filelight/
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/filelight/
%lang(es) %{tde_prefix}/share/doc/tde/HTML/es/filelight/
%lang(et) %{tde_prefix}/share/doc/tde/HTML/et/filelight/
%lang(it) %{tde_prefix}/share/doc/tde/HTML/it/filelight/
%lang(pt) %{tde_prefix}/share/doc/tde/HTML/pt/filelight/
%lang(ru) %{tde_prefix}/share/doc/tde/HTML/ru/filelight/
%lang(sv) %{tde_prefix}/share/doc/tde/HTML/sv/filelight/
%{tde_prefix}/share/man/man1/filelight.1*

