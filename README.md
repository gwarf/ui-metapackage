# User Interface (UI) meta-package

> In order to interact with
> [High Throughput Compute (HTC)](https://docs.egi.eu/users/compute/high-throughput-compute/)
> resources, you should have access to a `User Interface`, often referred to as
> a `UI`. This software environment will provide all the tools required to
> interact with the different middleware, as different sites can be using
> different Computing Element (CE), such as HTCondorCE and ARC-CE (CREAM is a
> legacy software stack that is not officially supported).

The UI contains a suite of clients and APIs that users and applications can use
to access
[High Throughput Compute](https://docs.egi.eu/users/compute/high-throughput-compute/)
services.

It will also install the
[IGTF distribution](https://docs.egi.eu/providers/operations-manuals/howto01_using_igtf_ca_distribution/).

The package relies on packages available in the following repositories:

- [UMD](https://go.egi.eu/umd)
- [EPEL](https://docs.fedoraproject.org/en-US/epel/)

## Installing and using the UI

Once the UI will be installed, you will need to set it up so to be able to
interact with the resources available to a given
[Virtual Organisation (VO)](https://ims.egi.eu/display/EGIG/Virtual+organisation).

### Deploying the UI

The UI is available as a package in the [UMD](https://go.egi.eu/umd) software
distribution, but it will also require additional software and configuration.

In order to help with deploying the UI, different solutions are possible:

- Deploying the UI manually, using the packages available from
  [UMD repositories](https://go.egi.eu/umd). Once the repositories are configured
  by install the `umd-release` package, install the `ui` meta-package, and
  configure the system to interact with the VOMS servers of the VO to be used.

  ```shell
  # Install EPEL repository
  $ yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
  # Install UMD repositories, look for available UMD release on https://repository.egi.eu/
  $ yum install -y http://repository.egi.eu/sw/production/umd/4/centos7/x86_64/updates/umd-release-4.1.3-1.el7.centos.noarch.rpm
  $ yum localinstall -y ui-*.rpm
  ```

- Some
  [Ansible roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
  are available in the
  [EGI Federation GitHub organisation](https://github.com/EGI-Federation?q=ansible-role),
  mainly [ansible-role-ui](https://github.com/EGI-Federation/ansible-role-ui)
  that should be used together with
  [ansible-role-VOMS-client](https://github.com/EGI-Federation/ansible-role-VOMS-client),
  providing software and material required for the authentication and
  authorisation, and
  [ansible-role-umd](https://github.com/EGI-Federation/ansible-role-umd)
  configuring the software repositories from where all the software will be
  installed.
- The repository
  [ui-deployment](https://github.com/EGI-Federation/ui-deployment) provides a
  [terraform](https://terraform.io)-based deployment allowing to deploy a
  `User Interface (UI)` in a
  [Cloud Compute virtual machine](https://docs.egi.eu/users/compute/cloud-compute/).
  This integrated deployment is based on the Ansible modules, and should be
  adjusted to your environment and needs.

### Manually configuring for a specific VO

If you have installed the `ui` meta-package manually, from
[UMD repository](https://repository.egi.eu/), you need to configure the support
of the VO(s) you want to use on the UI.

- Look for the VO ID card for the VO you want to use on the
  [Operations Portal](https://operations-portal.egi.eu/vo/)
  - You can also infer the URL from the VO name: for `dteam` the VO ID Card is
    available at
    [https://operations-portal.egi.eu/vo/view/voname/dteam](https://operations-portal.egi.eu/vo/view/voname/dteam).
- Access the VO-specific VOMS server, the VOMS server should be the one
  mentioned in the `Registry Information` section of the VO ID card. For your
  convenience, you should be able to use the link in the `Enrolment URL`.
  - For `dteam` it's
    [https://voms2.hellasgrid.gr:8443/voms/dteam/](https://voms2.hellasgrid.gr:8443/voms/dteam/).
- Once on the VOMS server, open the section `Configuration Info`.
  - For `dteam` it's the page
    [https://voms2.hellasgrid.gr:8443/voms/dteam/configuration/configuration.action](https://voms2.hellasgrid.gr:8443/voms/dteam/configuration/configuration.action).

The VOMS configuration pages contains the information required to configure your
UI so that it can interact with the VOMS server for your VO.

- As an example with `dteam` VO, you can find the VOMS server address in
  [the dteam VO ID card](https://operations-portal.egi.eu/vo/view/voname/dteam).
- Then looking at
  [dteam VOMS' Configuration page](https://voms2.hellasgrid.gr:8443/voms/dteam/configuration/configuration.action),
  you can create:

  - `/etc/vomsdir/<vo-name>/<voms-hostname>.lsc`, adjusting the file name
    according to the VO.

    - For `dteam`, the VOMS server is `voms2.hellasgrid.gr`, so the file would
      be named `/etc/grid-security/vomsdir/dteam/voms2.hellasgrid.gr.lsc` with
      the content for the **LSC configuration**.

      ```text
      /C=GR/O=HellasGrid/OU=hellasgrid.gr/CN=voms2.hellasgrid.gr
      /C=GR/O=HellasGrid/OU=Certification Authorities/CN=HellasGrid CA 2016
      ```

  - `/etc/vomses/<vo-name>-<voms-hosntame>` file, adjusting the file name
    according to the VO

    - For `dteam`, the VOMS server is `voms2.hellasgrid.gr`, so the file would
      be named `/etc/vomses/dteam-voms2.hellasgrid.gr` with the content of the
      **VOMSES string**.

      ```text
      "dteam" "voms2.hellasgrid.gr" "15004" "/C=GR/O=HellasGrid/OU=hellasgrid.gr/CN=voms2.hellasgrid.gr" "dteam"
      ```

If you cannot edit content in `/etc/vomses` and `/etc/grid-security/vomsdir`,
you can respectively use `~/.glite/vomses` and `~/.glite/vomsdir`. You may have
to export `X509_VOMSES` and `X509_VOMS_DIR` in your shell, as documented
[on CERN's twiki](https://twiki.cern.ch/twiki/bin/view/DREAM/GridSetup):

```shell
$ export X509_VOMSES=~/.glite/vomses
$ export X509_VOMS_DIR=~/.glite/vomsdir
```

### Setting up a UI using Ansible

If you are using Ansible, the following roles can be used:

- [egi_federation.ansible_role_umd](https://galaxy.ansible.com/egi_federation/ansible_role_umd),
  to configure the [UMD repository](https://repository.egi.eu)
- [egi_federation.ansible_role_voms-client](https://galaxy.ansible.com/egi_federation/ansible_role_voms_client),
  to configure the VOMS client for all known production VOs
- [egi_federation.ui](https://galaxy.ansible.com/egi_federation/ui), to
  configure the UI.

The repository [ui-deployment](https://github.com/EGI-Federation/ui-deployment)
provides a [terraform](https://terraform.io) based deployment allowing to deploy
a `User Interface (UI)` in a
[Cloud Compute virtual machine](https://docs.egi.eu/users/compute/cloud-compute/).
This integrated deployment is based on the Ansible modules, and should be
adjusted to your environment and needs.

## Building packages

### Building the RPM

The required build dependencies are:

- rpm-build
- make
- rsync

```shell
# Checkout tag to be packaged
$ git clone https://github.com/EGI-Federation/ui-metapackage.git
$ cd ui-metapackage
$ git checkout X.X.X
# Building in a container
$ docker run --rm -v $(pwd):/source -it quay.io/centos/centos:7
[root@bc96d4c5a232 /]# yum install -y rpm-build make rsync rpmlint
[root@bc96d4c5a232 /]# cd /source && make rpm
[root@bc96d4c5a232 /]# rpmlint --file .rpmlint.ini build/RPMS/x86_64/*.rpm
```

The RPM will be available into the `build/RPMS` directory.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in `ui.spec`
  - Updating version and changelog in `CHANGELOG`
- Once the PR has been merged, publish a new release using GitHub web interface
  - Suffix the tag name to be created with `v`, like `v1.0.0`
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project. This is now hosted
[on GitHub](https://github.com/EGI-Federation/ui-metapackage), and maintained by
the [EGI](https://www.egi.eu) Federation.
