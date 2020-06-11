Name:           lvtk2
Version:        2.0.0
Release:        0.rc1.1%{?dist}
Summary:        C++ Wrapper for LV2

License:        ISC
URL:            https://github.com/lvtk/lvtk
Source0:        https://github.com/lvtk/lvtk/archive/%{version}rc1.tar.gz

BuildRequires:  python3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconf-pkg-config
BuildRequires:  lv2-devel

%description
This software package contains libraries that wrap the LV2 C API and
extensions into easy to use C++ classes.

%package devel
Summary:        LVTK development files

%description devel
This package holds header files for building programs that link against LVTK.

%prep
%autosetup -n lvtk-2.0.0rc1

%build
python3 waf configure --prefix=%{buildroot}%{_prefix} \
 --libdir=%{buildroot}%{_libdir} --debug --bundle=lvtk-2.lv2
python3 waf build

# Remove buildroot from lvtk-2.pc
sed -i 's|^prefix=.*|prefix=/usr|' build/lvtk-2.pc

%install
rm -rf $RPM_BUILD_ROOT
python3 waf install

%files
%license COPYING
%doc README.md ChangeLog AUTHORS
%{_libdir}/lv2/lvtk-plugins.lv2/manifest.ttl
%{_libdir}/lv2/lvtk-plugins.lv2/volume.so
%{_libdir}/lv2/lvtk-plugins.lv2/volume.ttl
%{_libdir}/lv2/lvtk-2.lv2/manifest.ttl

%files devel
%{_includedir}/lvtk-2/lvtk/*.hpp
%{_includedir}/lvtk-2/lvtk/*.h
%{_includedir}/lvtk-2/lvtk/ext/*.hpp
%{_includedir}/lvtk-2/lvtk/ext/ui/*.hpp
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jun 11 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> 2.0.0-0.rc1.1
- Initial build
