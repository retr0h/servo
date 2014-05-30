# encoding: UTF-8
#
# Cookbook Name:: servo-nsq
# Recipe:: default
#
# Copyright 2014, John Dewey
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

Chef::Recipe.send(:include, ServoNSQ::Helpers)

address = address_for node['servo-nsq']['bind_interface']

node.override['nsq']['nsqd']['broadcast_address'] = address
node.override['nsq']['nsqlookupd']['broadcast_address'] = address
node.override['nsq']['nsqlookupd']['tcp_address'] = "#{address}:4160"

include_recipe 'nsq::nsqadmin'
include_recipe 'nsq::nsqd'
include_recipe 'nsq::nsqlookupd'
