srcdir = spp-ads1115

all:
	make -C ${srcdir}

DESTDIR    ?=
prefix     ?= $(DESTDIR)/usr
bindir     ?= $(prefix)/bin

install: all
	install -D -m755 ${srcdir}/ads1115 -t ${bindir}
