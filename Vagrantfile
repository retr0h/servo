Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.omnibus.chef_version = "latest"

  config.vm.define "broker1" do |c|
    c.vm.host_name = "broker1"
    c.vm.network "private_network", ip: "192.168.90.5"
    c.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
    end

    c.vm.provision "chef_solo" do |chef|
      chef.cookbooks_path = "vagrant/cookbooks"
      chef.custom_config_path = "vagrant/solo.rb"
      chef.add_recipe "apt"
      chef.add_recipe "java"
      chef.add_recipe "kafka::zookeeper"
      chef.add_recipe "kafka::server"
    end
  end
end
