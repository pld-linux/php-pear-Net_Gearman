%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Gearman
%define		_status		alpha
%define		_pearname	Net_Gearman
Summary:	%{_pearname} - A PHP interface to Danga's Gearman
Summary(pl.UTF-8):	%{_pearname} - interfejs PHP do systemu Gearman
Name:		php-pear-%{_pearname}
Version:	0.2.3
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bc5402ede86d7de797abe712dc538573
URL:		http://pear.php.net/package/Net_Gearman/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gearman (http://www.danga.com/gearman) is a system to farm out work to
other machines. It can load balance function calls to lots of machines
and allows you to call functions between languages. It can also run
all function calls in parallel.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Gearman (http://www.danga.com/gearman) to system do dystrubucji zadań
na inne maszyny. Możliwe jest rozdzielanie wywołań funkcji na wiele
maszyn jak również na wywoływanie funkcji pomiędzy różnymi językami.
Możliwe jest także wywołanie wielu funkcji równolegle.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Net_Gearman/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Gearman

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Net_Gearman
