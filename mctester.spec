### RPM external mctester 1.25.0a

Source:  http://service-spi.web.cern.ch/service-spi/external/MCGenerators/distribution/%n-%realversion-src.tgz

Requires: hepmc
Requires: root

BuildRequires: autotools

%define keep_archives true

%if "%{?cms_cxx:set}" != "set"
%define cms_cxx g++
%endif

%if "%{?cms_cxxflags:set}" != "set"
%define cms_cxxflags -O2 -std=c++0x
%endif

%prep
%setup -q -n %{n}/%{realversion}

./configure \
  --with-HepMC=${HEPMC_ROOT} \
  --with-root=${ROOT_ROOT} \
  --prefix=%i \
  CXX="%cms_cxx" \
  CXXFLAGS="%cms_cxxflags"

%build
make

%install
make install

%ifos darwin
find %i/lib -name "*.dylib" -exec install_name_tool -change '../lib/libHEPEvent.dylib' 'libHEPEvent.dylib' {} \;
%endif
