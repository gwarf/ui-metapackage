Name:		ui
Version:	4.0.3
Release:	1%{?dist}
Summary:	UI meta-packages
Group:		Applications/Internet
License:	ASL 2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

# the above replaced by ca-policy-egi-core
Requires:       ca-policy-egi-core
Requires:       aria2
Requires:	      davix-libs
Requires:       dcache-srmclient
Requires:       dcap
Requires:	      dcap-devel
Requires:	      dcap-libs 
Requires:	      dcap-tunnel-gsi
Requires:	      dcap-tunnel-krb  
Requires:	      dcap-tunnel-ssl  
Requires:	      dcap-tunnel-telnet
Requires:	      fetch-crl
Requires:	      fts-client
Requires:     	 fuse
Requires:       fuse-libs
Requires:       gfal2-all
Requires:	      gfal2-plugin-xrootd
Requires:       gfal2-python
Requires:	      gfal2-util
Requires:       gfalFS
Requires:	      gfal2-doc
Requires:	      gfal2-devel
Requires:	      ginfo
Requires:       glite-ce-cream-cli  
Requires:       glite-ce-cream-client-api-c
Requires:	      glite-yaim-core
Requires:	      glite-yaim-clients
Requires:	      gsi-openssh-clients
Requires:	      globus-gsi-cert-utils-progs
Requires:       lcg-ManageVOTag  
Requires:       lcg-info  
Requires:       lcg-infosites  
Requires:       lcg-tags  
Requires:	      myproxy
Requires:       nordugrid-arc-client
Requires:       nordugrid-arc-plugins-xrootd
Requires:       nordugrid-arc-plugins-gfal
Requires:	      nordugrid-arc-plugins-globus
Requires:	      nordugrid-arc-plugins-needed
Requires:       openldap-clients
Requires:       voms  
Requires:       voms-clients-java  
Requires:	      xrootd-client

Source:		       ui-4.0.3.tar.gz

%description
Suite of clients and APIs that users and applications 
can use to access grid services

%prep

%build
# Nothing to do

%install
rm -rf $RPM_BUILD_ROOT
 mkdir -p $RPM_BUILD_ROOT
 find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
 find $RPM_BUILD_ROOT -name '*.pc' -exec sed -i -e "s|$RPM_BUILD_ROOT||g" {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%changelog
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
