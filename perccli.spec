%define	ver	7.3_007.0318
%define dver	%(echo %{version} | tr '_' '-')
Summary:	Proprietary controller binary for DELL PERC RAID cards
Name:		perccli
Version:	%{ver}
Release:	1
License:	Unknown
Group:		Base
# link from any lastest download
Source0:	https://dl.dell.com/FOLDER04830419M/1/%{name}_%{dver}_linux.tar.gz
# Source0-md5:	1cd2a854c1a3a83c87b83086543f9897
URL:		https://www.dell.com/support/home/us/en/04/drivers/driversdetails?driverid=f48c2
BuildRequires:	rpm-utils
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin
%define		_enable_debug_packages	0

%description
Proprietary controller binary for DELL PERC RAID cards.

%prep
%setup -q -n %{name}_%{dver}_linux
rpm2cpio Linux/*.rpm | cpio -i -d

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%ifarch %{ix86}
install -p ./opt/MegaRAID/perccli/perccli $RPM_BUILD_ROOT%{_sbindir}/perccli
%endif

%ifarch %{x8664}
install -p ./opt/MegaRAID/perccli/perccli64 $RPM_BUILD_ROOT%{_sbindir}/perccli
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt
%attr(755,root,root) %{_sbindir}/perccli
