def get_address index
  "192.168.90.#{10+index}"
end

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.omnibus.chef_version = "latest"

  instances = (1..3)
  instances.each do |instance|
    vm_name = "nsqd-#{instance}"
    config.vm.define vm_name do |c|
      c.vm.host_name = vm_name
      c.vm.network "private_network", ip: get_address(instance) # eth1
      c.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--memory", "512"]
      end
      c.vm.provision "chef_solo" do |chef|
        chef.cookbooks_path = "vagrant/cookbooks"
        chef.custom_config_path = "vagrant/solo.rb"
        chef.add_recipe "apt"
        chef.add_recipe "servo-nsq"

        chef.json = {
          nsq: {
            nsqd: {
              lookupd_tcp_address: instances.map { |i| "#{get_address(i)}:4160" },
              lookupd_http_address: instances.map { |i| "#{get_address(i)}:4161" }
            }
          }
        }
      end
    end
  end
end
