#as LF

NAME= $(shell grep Name: ui.spec | sed 's/^[^:]*:[^a-zA-Z]*//' )
VERSION= $(shell grep Version: ui.spec | sed 's/^[^:]*:[^0-9]*//' )
RELEASE= $(shell grep Release: ui.spec |cut -d"%" -f1 |sed 's/^[^:]*:[^0-9]*//')
build=$(shell pwd)/build
DATE=$(shell date "+%a, %d %b %Y %T %z")
dist=$(shell rpm --eval '%dist' | sed 's/.cern/''/')

default:
	@echo "Nothing to do"

#_builddir  := rpmbuild/BUILD/
#_specdir   := rpmbuild/SPECS/
#_sourcedir := rpmbuild/SOURCES/
#_rpmdir    := rpmbuild/RPMS/

dist:
	@mkdir -p  $(build)/$(NAME)-$(VERSION)/
	rsync -a --exclude ".svn" --exclude "$(build)" * $(build)/$(NAME)-$(VERSION)/
	cd $(build); tar --exclude "$(NAME)-$(VERSION)/build" --exclude "$(NAME)-$(VERSION)/build/*" -czvf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/; cd -

sources: dist
	cp $(build)/$(NAME)-$(VERSION).tar.gz .

prepare: dist
	@mkdir -p  $(build)/RPMS/noarch
	@mkdir -p  $(build)/SRPMS/
	@mkdir -p  $(build)/SPECS/
	@mkdir -p  $(build)/SOURCES/
	@mkdir -p  $(build)/BUILD/
	cp $(build)/$(NAME)-$(VERSION).tar.gz $(build)/SOURCES

srpm: prepare
	rpmbuild -bs --define="dist ${dist}" --define='_topdir ${build}' $(NAME).spec

rpm: srpm
	rpmbuild --rebuild  --define="dist ${dist}" --define='_topdir ${build} ' $(build)/SRPMS/$(NAME)-$(VERSION)-$(RELEASE)${dist}.src.rpm

clean:
	rm -f *~ $(NAME)-$(VERSION).tar.gz
	rm -rf $(build)

.PHONY: dist srpm rpm sources clean
