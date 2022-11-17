# UI metapackage

Suite of clients and APIs that users and applications can use to access
[High Throughput Compute](https://docs.egi.eu/users/compute/high-throughput-compute/)
services.

## Building packages

### Building a RPM

The required build dependencies are:

- rpm-build
- make
- rsync

```shell
# Checkout tag to be packaged
git clone https://github.com/EGI-Federation/ui-metapackage.git
cd ui-metapackage
git checkout X.X.X
# Building in a container
docker run --rm -v $(pwd):/source -it centos:7
yum install -y rpm-build make rsync
cd /source && make rpm
```

The RPM will be available into the `build/RPMS` directory.

## Preparing a release

- Prepare a changelog from the last version, including contributors' names
- Prepare a PR with
  - Updating version and changelog in `ui-metapackage.spec`
  - Updating version and changelog in `CHANGELOG`
- Once the PR has been merged, publish a new release using GitHub web interface
  - Packages will be built using GitHub Actions and attached to the release page

## History

This work started under the EGEE project. This is now hosted here on GitHub, and
maintained by the EGI Federation.
