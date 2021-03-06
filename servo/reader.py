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


class Reader(object):
    """
    A client which handles read interactions with nsqd.
    """

    def __init__(self, config, **kwargs):
        self._config = config

    def _handler(self, message):
        msg = ('- {0}:\n'
               '  {1}\n'
               '  {2}\n').format(message.id,
                                 message.body,
                                 message.attempts)
        print msg
        return True

    def _set_reader(self):
        lookupd_poll_interval = self._config.reader_lookupd_poll_interval
        nsq.Reader(message_handler=self._handler,
                   lookupd_http_addresses=self._config.reader_hosts,
                   topic=self._config.reader_topic,
                   channel=self._config.reader_channel,
                   lookupd_poll_interval=lookupd_poll_interval)

    def run(self):
        self._set_reader()
        nsq.run()
