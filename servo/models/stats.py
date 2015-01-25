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

from cqlengine import columns
from cqlengine.models import Model


class Stats(Model):
    read_repair_chance = 0.05
    updated_at = columns.DateTime(primary_key=True)
    # updated_at = columns.DateTime
    # year = columns.Integer(primary_key=True, partition_key=True)
    # month = columns.Integer(primary_key=True, partition_key=True)
    # date = columns.Integer(primary_key=True, partition_key=True)
    # region = columns.Text(primary_key=True)
    # availability_zone = columns.Text(primary_key=True)
    # service = columns.Text(primary_key=True)
    # current_state = columns.Integer
    # current_message = columns.Integer
    # worst_state = columns.Integer
    # worst_message = columns.Integer
    # states = columns.List(columns.Text)

# from cqlengine import connection
# connection.setup(['192.168.90.11'], 'servo_test')
# from datetime import datetime
# Stats.create(updated_at=datetime.now())
