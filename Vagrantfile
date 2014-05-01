Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.omnibus.chef_version = "latest"

  config.vm.define "nsq" do |c|
    c.vm.host_name = "nsq"
    c.vm.network "private_network", ip: "192.168.90.5"
    c.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
    end

    c.vm.provision "chef_solo" do |chef|
      chef.cookbooks_path = "vagrant/cookbooks"
      chef.custom_config_path = "vagrant/solo.rb"
      chef.add_recipe "apt"
      chef.add_recipe "golang"
      chef.add_recipe "nsq::nsqadmin"
      chef.add_recipe "nsq::nsqd"
      chef.add_recipe "nsq::nsqlookupd"

      chef.json = {
        nsq: {
          nsqd: {
            lookupd_tcp_address: ["192.168.90.5:4160"],
            lookupd_http_address: ["192.168.90.5:4161"]
          }
        }
      }
    end
  end
end
