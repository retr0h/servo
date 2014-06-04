all: deps

deps:
	git submodule update --init

.PNONY: all deps test
