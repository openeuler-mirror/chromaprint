Name:           chromaprint
Version:        1.4.2
Release:        4
Summary:        Library implementing the AcoustID fingerprinting
License:        GPLv2+
URL:            http://www.acoustid.org/chromaprint
Source0:        https://github.com/acoustid/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ cmake fftw-devel >= 3

%description
Chromaprint is the core component of the AcoustID project. It's a client-side library that implements a
custom algorithm for extracting fingerprints from any audio source.

The library exposes a simple C API. The documentation for the C API can be found in chromaprint.h.

Note that the library only calculates audio fingerprints from the provided raw uncompressed audio data.
It does not deal with audio file formats in any way. Your application needs to find a way to decode audio
files (MP3, MP4, FLAC, etc.) and feed the uncompressed data to Chromaprint.

%package -n libchromaprint
Summary:        Library implementing the AcoustID fingerprinting
Obsoletes:      python-chromaprint < 0.6-3

%description -n libchromaprint
Chromaprint is the core component of the AcoustID project. It's a client-side library that implements a
custom algorithm for extracting fingerprints from any audio source.

The library exposes a simple C API. The documentation for the C API can be found in chromaprint.h.

Note that the library only calculates audio fingerprints from the provided raw uncompressed audio data.
It does not deal with audio file formats in any way. Your application needs to find a way to decode audio
files (MP3, MP4, FLAC, etc.) and feed the uncompressed data to Chromaprint.

%package -n libchromaprint-devel
Summary:        Headers for developing programs that will use chromaprint
Requires:       libchromaprint = %{version}-%{release}

%description -n libchromaprint-devel
This package contains header files for developing applications which use chromaprint.

The library exposes a simple C API. The documentation for the C API can be found in chromaprint.h.

%prep
%autosetup -n %{name}-%{version} -p1
%{cmake} -DBUILD_EXAMPLES=OFF -DBUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release -DBUILD_TOOLS=OFF

%build
%make_build

%install
%make_install
%delete_la

%post -n libchromaprint
/sbin/ldconfig

%postun -n libchromaprint
/sbin/ldconfig

%files -n libchromaprint
%doc LICENSE.md NEWS.txt README.md
%{_libdir}/lib*.so.*

%files -n libchromaprint-devel
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Dec  3 2019 lingsheng <lingsheng@huawei.com> - 1.4.2-4
- Package init
