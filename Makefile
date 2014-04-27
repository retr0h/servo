all: deps

deps:
	git submodule init
	git submodule update
	go get -d -v ./...

test: deps
	go list ./... | xargs -n1 go test

.PNONY: all deps test
