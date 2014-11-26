servo
=====

The Latin Word Servo has many meanings, mainly: to watch over, keep, protect, observe, save, reserve.

Developing
==========

Add the following to ~/.vimrc:

	set rtp+=$GOROOT/misc/vim
	autocmd FileType go autocmd BufWritePre <buffer> Fmt

Running:

	$ mkdir -p $GOPATH/src/github.com/retr0h
	$ cd !$
	$ git clone git@github.com:retr0h/servo.git
	$ cd servo
  $ make
	$ vagrant up

In one window.  Publish an initial message, and create the topic:

	$ curl -d 'hello world 1' 'http://192.168.90.11:4151/put?topic=test'

In the same window, start the client:

	nsq_to_file --topic=test --output-dir=/tmp --lookupd-http-address=192.168.90.11:4161

In another window, publish more messages:
 
	curl -d 'hello world 2' 'http://192.168.90.11:4151/put?topic=test'

License
=======

MIT
