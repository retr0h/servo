# encoding: UTF-8

Vagrant.configure('2') do |config|
  config.vm.box = 'hashicorp/precise64'
  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'vagrant/site.yml'
    ansible.limit = 'all'
    ansible.sudo = true
    ansible.host_key_checking = false
    # ansible.verbose = "vvv"
    ansible.extra_vars = {
      cassandra_listen_address: '192.168.90.11',
      cassandra_rpc_address: '192.168.90.11',
      cassandra_seeds: [
        '192.168.90.11'
      ],
      limits_limits: [
        "* - nofile 100000",
        "* - memlock unlimited",
        "* - nproc 32768",
        "* - as unlimited",
        "* soft nofile 32768",
        "* hard nofile 32768",
        "root soft nofile 32768",
        "root hard nofile 32768"
      ]
    }
  end

  config.vm.define 'cassandra' do |c|
    c.vm.host_name = 'cassandra'
    c.vm.network 'private_network', ip: '192.168.90.11' # eth1
    c.vm.provider 'virtualbox' do |vb|
      vb.customize ['modifyvm', :id, '--memory', '2048']
    end
  end
end
