Name:		emi-ui
Version:	3.1.0
Release:	1%{?dist}
Summary:	EMI UI meta-packages
Group:		Applications/Internet
License:	ASL 2.0
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       ca_policy_igtf-classic  
Requires:       ca_policy_igtf-mics  
Requires:       ca_policy_igtf-slcs  
Requires:       dcache-srmclient
Requires:       dcap
Requires:	dcap-devel
Requires:	dcap-libs 
Requires:	dcap-tunnel-gsi
Requires:	dcap-tunnel-krb  
Requires:	dcap-tunnel-ssl  
Requires:	dcap-tunnel-telnet
#Requires:       delegation-cli
Requires:       dpm
Requires:       libdpm.so.1()(64bit), libdpm.so.1, dpm-libs
Requires:       dpm-devel
Requires:       dpm-perl
Requires:       dpm-python
%if "%{?dist}" == ".el5"
Requires:       dpm-python26
%endif
Requires:       emi-version
Requires:       emi.amga.amga-cli
Requires:       emi.saga-adapter.context-cpp  
Requires:       emi.saga-adapter.isn-cpp  
Requires:       emi.saga-adapter.sd-cpp  
Requires:	fetch-crl
Requires:       fts2-client
Requires:       libgfal.so.1()(64bit), libgfal.so.1, gfal
Requires:       gfal-python
%if "%{?dist}" == ".el5"
Requires:       gfal-py26
%endif  
Requires:       gfal2-all
Requires:       gfal2-python
Requires:	gfal2-util
Requires:       gfalFS
Requires:	gfal2-doc
Requires:	gfal2-devel
Requires:	ginfo
Requires:       glite-ce-cream-cli  
Requires:       glite-ce-cream-client-api-c
Requires:       glite-ce-monitor-cli  
Requires:       glite-ce-monitor-client-api-c  
Requires:       glite-jdl-api-cpp  
Requires:       glite-jobid-api-c  
Requires:       glite-lb-client
Requires:	glite-lb-client-progs 
Requires:       glite-lb-common  
Requires:       glite-lbjp-common-gss  
Requires:       glite-lbjp-common-trio  
Requires:       glite-service-discovery-api-c  
Requires:       glite-wms-brokerinfo-access  
Requires:       glite-wms-ui-commands  
Requires:	glite-yaim-core
Requires:	glite-yaim-clients
Requires:       gridsite-commands
Requires:       gridsite-libs
Requires:	gsi-openssh-clients
Requires:	globus-gsi-cert-utils-progs
Requires:       lcgdm-devel
%ifarch x86_64
%if 0%{?fedora} > 10 || 0%{?rhel}>5
Requires:       lcgdm-devel(x86-32)
%else
## EL 5 fix, force install of lcgdm-devel 32 bits
Requires:	/usr/lib/liblcgdm.so
%endif
%endif
Requires:       liblcgdm.so.1()(64bit), liblcgdm.so.1, lcgdm-libs
Requires:       lcg-ManageVOTag  
Requires:       lcg-info  
Requires:       lcg-infosites  
Requires:       lcg-tags  
Requires:       lcg-util
Requires:       liblcg_util.so.1()(64bit), liblcg_util.so.1, lcg-util-libs
Requires:       lcg-util-python
%if "%{?dist}" == ".el5"
Requires:       lcg-util-py26
%endif
Requires:       lfc
Requires:       liblfc.so.1()(64bit), liblfc.so.1, lfc-libs
Requires:       lfc-devel
Requires:       lfc-perl
Requires:       lfc-python
%if "%{?dist}" == ".el5"
Requires:       lfc-python26
%endif
Requires:	myproxy
Requires:       nordugrid-arc-client-tools  
Requires:       nordugrid-arc-plugins-xrootd
Requires:       nordugrid-arc-plugins-gfal
Requires:       openldap-clients
Requires:       storm-srm-client  
Requires:       unicore-hila-shell  
Requires:       unicore-hila-unicore6  
Requires:       unicore-hila-emi-es
Requires:       unicore-hila-gridftp
Requires:       unicore-ucc
#Requires:       transfer-cli
#Requires:	util-c  
Requires:       voms  
Requires:       voms-clients3  
Source:		emi-ui-3.1.0.tar.gz

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

