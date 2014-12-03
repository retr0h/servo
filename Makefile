all: deps up test

deps:
	@git submodule update --init

up:
	@vagrant up --no-provision
	@vagrant provision 
	
test:
	@tox

.PNONY: all deps up test
