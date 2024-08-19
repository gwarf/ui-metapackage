%global debug_package %{nil}

Name: ui
Version: 6.2.0
Release: 1%{?dist}
Summary: User Interface meta-package
Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/EGI-Federation/ui-metapackage
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build

Requires: ca-policy-egi-core
Requires: aria2
Requires: cvmfs
Requires: davix-libs
Requires: fetch-crl
Requires: condor
%if 0%{?rhel} == 7
Requires: gfalFS
Requires: dcache-srmclient
Requires: lcg-ManageVOTag
Requires: lcg-info
Requires: lcg-tags
Requires: fts-client
%endif
Requires: dcap
Requires: dcap-devel
Requires: dcap-libs
Requires: dcap-tunnel-gsi
Requires: dcap-tunnel-krb
Requires: dcap-tunnel-ssl
Requires: dcap-tunnel-telnet
Requires: fuse
Requires: fuse-libs
Requires: gfal2-all
%if 0%{?rhel} == 7
Requires: gfal2-python
Requires: gfal2-util
%else
Requires: python3-gfal2
Requires: python3-gfal2-util
%endif
Requires: gfal2-doc
Requires: gfal2-devel
Requires: ginfo
Requires: gsi-openssh-clients
Requires: globus-gsi-cert-utils-progs
Requires: lcg-infosites
Requires: myproxy
Requires: nordugrid-arc-client
Requires: nordugrid-arc-plugins-xrootd
Requires: nordugrid-arc-plugins-gfal
Requires: nordugrid-arc-plugins-globus
Requires: nordugrid-arc-plugins-needed
Requires: nordugrid-arc-plugins-arcrest
Requires: openldap-clients
Requires: voms
Requires: voms-clients-java
Requires: xrootd-client

%description
Suite of clients and APIs that users and applications
can use to access grid services

%prep

%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc /usr/share/doc/ui/README.md

%changelog
* Tue Jun 18 2024 <baptiste.grenier@egi.eu> - 6.2.0-1
- Include CVMFS as a dependency (#12) (Baptiste Grenier)
* Tue Jun 11 2024 <baptiste.grenier@egi.eu> - 6.1.0-1
- Build and package for RHEL8 (#11) (Baptiste Grenier)
* Mon Jun 10 2024 <baptiste.grenier@egi.eu> - 6.0.1-1
- Add ARC REST, ginfo and lcg-infosites on RHEL9 (#10) (Baptiste Grenier)
* Tue Jun 04 2024 <andrea.manzi@egi.eu> - 6.0.0-1
- Support for El9 (#6) (Andrea Manzi)
* Fri Nov 18 2022 Baptiste Grenier <baptiste.grenier@egi.eu> - 5.0.0-1
- Drop support for RHEL6, CREAM, LFC, DPM, YAIM (#2) (Baptiste Grenier)
* Fri Sep 15 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.3-1
- package renamed to ui
* Thu Apr 20 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.2-1
- added cream-cli and yaim on el7
* Thu Mar 09 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.1-1
- added dcachesrm-client on el7
* Tue Sep 13 2016 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.0-1
- removed EL5 support
- added EL7 support
* Sun Sep 07 2014 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.1.0-1
- added dependecies on gfal2-util and ginfo (IGIRTC-176)
* Mon Sep 09 2013 Adrien Devresse <adevress at cern.ch> - 3.0.3-1
- fix for lcgdm-devel 32 bits dependency problem on EL5
* Sun Jul 28 2013 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.0.2-1
- added forgotten dependencies globus-gsi-cert-utils-progs (IGIRTC-156)
* Fri Apr 19 2013 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.0.1-1
- added missing dependencies gsi-openssh-clients and glite-ce-monitor-cli
* Fri Feb 15 2013 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.0.0-1
- removed glite-wms-wmproxy-api-java, glite-wms-wmproxy-api-python - unsupported in EMI 3
* Sun Feb 03 2013 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.0.0-0
- updated deps according to DM Integration/Clients - add fts2-client
- updated deps according the EMI3Arc - add *-xrootd, *-gfal
- replaced all nordugrid-arc-* with nordugrid-arc-client-tools
- removed nordugrid-arc-compat
- updated deps according the EMI3VOMS - replace voms-clients with voms-clients3
- added unicore-hila-emi-es, *-gridftp
- removed deps on emi-trustmanager-* - clients/apis should already have these deps
* Thu Oct 11 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.1-1
- passing to the final versioning
* Fri Oct 05 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-4
- Updated deps according to DM Integration/Clients
* Fri Aug 31 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-3
- Added missing dependencis to the EMI 2 version (includes 32b)
* Fri Apr 01 2011 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 1.0.0-0
- First version for EMI
