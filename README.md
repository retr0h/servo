servo
=====

The Latin Word Servo has many meanings, mainly: to watch over, keep, protect, observe, save, reserve.

Developing
==========

Add the following to ~/.vimrc:

    set rtp+=$GOROOT/misc/vim
    autocmd FileType go autocmd BufWritePre <buffer> Fmt

Running:

    $ vagrant plugin install vagrant-omnibus
    $ mkdir -p $GOPATH/src/github.com/retr0h
    $ cd !$
    $ git clone git@github.com:retr0h/servo.git
    $ git submodule init
    $ git submodule update
    $ go get github.com/Shopify/sarama
    $ go get github.com/codegangsta/cli

    $ vagrant up

In one window:

    $ bin/kafka-console-consumer.sh \
        --zookeeper 192.168.90.5:2181 \
        --topic my_topic

In another window:

    $ go run cli/servo.go -a produce

License
=======

Author:: John Dewey (<john@dewey.ws>)

Copyright 2014, John Dewey

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
