# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2015 John Dewey
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

"""
Servo CLI tool.
"""

import argparse

import servo
from servo.app import api
from servo.client import Client


def _parse_args():
    ap = argparse.ArgumentParser(prog='servo',
                                 description=__doc__.strip())
    ap.add_argument('--version', action='version',
                    version=servo.__version__)
    ap.add_argument('--setup', action='store_true',
                    help='setup keyspace and schema')
    ap.add_argument('--teardown', action='store_true',
                    help='teardown keyspace')
    ap.add_argument('--server', action='store_true',
                    help='start API server')
    args = vars(ap.parse_args())
    return args


def main():
    args = _parse_args()

    config = {
        'hosts': ['192.168.90.11'],
        'keyspace': 'servo_test'
    }
    c = Client(config)
    c.lazy_connection()

    if args['setup']:
        c.setup()
    elif args['teardown']:
        c.teardown()
    elif args['server']:
        api.run()


if __name__ == '__main__':
    main()
