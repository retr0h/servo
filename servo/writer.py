# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2014 John Dewey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import nsq
import tornado.ioloop
import time


class Writer(object):
    """
    A client which handles write interactions with nsqd.
    """

    def __init__(self, **kwargs):
        # TODO(retr0h): Further abstract out into a config class.
        port = kwargs.get('port', 4150)
        self._nsqd_addrs = ['{host}:{port}'.format(**locals())
                            for host in kwargs.get('nsqd_addresses')]
        self._writer = self._get_writer()

    def _pub_message(self):
        self._writer.pub('nsq_reader',
                         time.strftime('%H:%M:%S'),
                         self._finish_pub)

    def _finish_pub(self, conn, data):
        print data

    def _get_writer(self):
        # TODO: HA should be handled by publishing to a known load balanced
        # endpoint or local nsqd instance.
        return nsq.Writer(self._nsqd_addrs)

    def _get_ioloop(self):
        return tornado.ioloop.PeriodicCallback(self._pub_message, 1000)

    def run(self):
        self._get_ioloop().start()
        nsq.run()
