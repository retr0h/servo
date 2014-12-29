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

import unittest2 as unittest
# from mock import Mock
# from mock import patch

from servo import util


class TestUtil(unittest.TestCase):
    def test_execute(self):
        cmd = ['test', 'true']
        result = util.execute(cmd)

        self.assertEquals(True, result)

    def test_execute_raises(self):
        cmd = ['ls', '/invalid']
        with self.assertRaises(Exception) as context:
            util.execute(cmd)

        # TODO(retr0h): Don't assume test OS.
        # OSX:
        # ls: /invalid: No such file or directory\n
        # Travis:
        # ls: cannot access /invalid: No such file or directory\n
        self.assertRegexpMatches(context.exception.message,
                                 r'.* No such file or directory\n')
