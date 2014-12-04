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

import json
import os


class Config(object):
    """
    A class which handles the configuration of servo.
    """

    def __init__(self, **kwargs):
        config_file = kwargs.get('config_file', '/etc/servo.json')
        self._config = self._get_config(config_file)

    @property
    def reader_hosts(self):
        port = self._get_reader_port()
        hosts = ['192.168.90.12',
                 '192.168.90.13',
                 '192.168.90.14']
        return self._get_connection_list(hosts, port)

    @property
    def writer_hosts(self):
        port = self._get_writer_port()
        hosts = ['192.168.90.12',
                 '192.168.90.13',
                 '192.168.90.14']
        return self._get_connection_list(hosts, port)

    @property
    def reader_lookupd_poll_interval(self):
        return self._config.get('reader_lookupd_poll_interval', 15)

    @property
    def reader_topic(self):
        return self._config.get('reader_topic', 'nsq_reader')

    @property
    def reader_channel(self):
        return self._config.get('reader_channel', 'asdf')

    def _get_config(self, config_file):
        if os.path.isfile(config_file):
            return json.load(open(config_file))
        else:
            return {}

    def _get_connection_list(self, hosts, port):
        """
        Create a connection object for `etcd.Client`.  Returns a tuple
        consisting of tuples in the form of (host, port).
        """
        return ['{host}:{port}'.format(**locals())
                for host in hosts]

    def _get_reader_port(self):
        return self._config.get('reader_port', 4161)

    def _get_writer_port(self):
        return self._config.get('reader_port', 4150)
