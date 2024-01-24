Name:         spp-ads1115
Version:      1.0
Release:      alt1

Summary:      SPP interface to ADS1113/1114/1115 ADC converter
Group:        System
URL:          https://github.com/slazav/spp-ads1115
License:      GPL

Packager:     Vladislav Zavjalov <slazav@altlinux.org>

Source:       %name-%version.tar
BuildRequires: gcc-c++

%description
SPP interface to ADS1113/1114/1115 ADC converter

%prep
%setup -q

%build
%make

%install
%makeinstall initdir=%buildroot%_initdir

%files
%_bindir/ads1115

%changelog
* Wed Jan 24 2024 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- This is stable version which was written in Feb 2021.
  I'm using this code (not SPP interface, but custom pmeas program)
  on the f4rpi RuspberryPi computer for collecting data from pressure sensors.
  In Jan 2024 the program was transferred from pico_rec repository to
  the separate repo https://github.com/slazav/spp-ads1115.
