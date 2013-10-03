Name:		emi-ui
Version:	2.0.3
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
Requires:       delegation-cli  
Requires:       dpm
Requires:       libdpm.so.1()(64bit), libdpm.so.1, dpm-libs
Requires:       dpm-devel
Requires:       dpm-perl
Requires:       dpm-python
%if "%{?dist}" == ".el5"
Requires:       dpm-python26
%endif
Requires:       emi-trustmanager  
Requires:       emi-trustmanager-tomcat  
Requires:       emi-version
Requires:       emi.amga.amga-cli
Requires:       emi.saga-adapter.context-cpp  
Requires:       emi.saga-adapter.isn-cpp  
Requires:       emi.saga-adapter.sd-cpp  
Requires:	fetch-crl
Requires:       libgfal.so.1()(64bit), libgfal.so.1, gfal
Requires:       gfal-python
%if "%{?dist}" == ".el5"
Requires:       gfal-py26
%endif  
Requires:       gfal2-all
Requires:       gfal2-python
Requires:       gfalFS
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
Requires:       glite-wms-wmproxy-api-java  
Requires:       glite-wms-wmproxy-api-python  
Requires:	glite-yaim-core
Requires:	glite-yaim-clients
Requires:	globus-gsi-cert-utils-progs
Requires:       gridsite-commands
Requires:       gridsite-libs
Requires:	gsi-openssh-clients
Requires:       lcgdm-devel
%if 0%{?fedora} > 10 || 0%{?rhel}>5
Requires: lcgdm-devel(x86-32)
%else
## EL 5 fix, force install of lcgdm-devel 32 bits
Requires: /usr/lib/liblcgdm.so
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
Requires:       nordugrid-arc-client  
Requires:       nordugrid-arc-compat  
Requires:       nordugrid-arc-java  
Requires:       nordugrid-arc-plugins-globus  
Requires:       nordugrid-arc-plugins-needed  
Requires:       nordugrid-arc-python  
Requires:       openldap-clients
Requires:       storm-srm-client  
Requires:       unicore-hila-shell  
Requires:       unicore-hila-unicore6  
Requires:       unicore-ucc
Requires:       transfer-cli
Requires:	util-c  
Requires:       voms  
Requires:       voms-clients  
Source:		emi-ui-2.0.3.tar.gz

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
* Thu Oct 03 2013  Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.3-1
- fix for lcgdm-devel 32 bits dependency problem on EL5 (thanks Adrien Devresse)
- added forgotten dependencies globus-gsi-cert-utils-progs (IGIRTC-156)
* Thu Oct 11 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.1-1
- passing to the final versioning
* Fri Oct 05 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-4
- Updated deps according to DM Integration/Clients
* Fri Aug 31 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-3
- Added missing dependencis to the EMI 2 version (includes 32b)
* Fri Apr 01 2011 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 1.0.0-0
- First version for EMI

