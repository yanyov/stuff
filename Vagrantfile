# -*- mode: ruby -*-
# vi: set ft=ruby :

$ip = "192.168.100.2"
$memory = "2048"
$cpus = 2
$disk_size = '50GB'

$script = <<-SCRIPT
echo '#{$ip}1  vm1' >> /etc/hosts
echo '#{$ip}2  vm2' >> /etc/hosts
echo '#{$ip}3  vm3' >> /etc/hosts
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
systemctl restart sshd
useradd -s /bin/bash -m ansible
echo "ansible ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers
mkdir ~ansible/.ssh
chmod 700 ~ansible/.ssh
cp /tmp/ssh/* ~ansible/.ssh
chown -R ansible: ~ansible/.ssh/
chmod 400 /home/ansible/.ssh/id_rsa
rm -rf /tmp/ssh/
export DEBIAN_FRONTEND=noninteractive
apt update; apt install -y python3-pip
pip3 install ansible
SCRIPT

Vagrant.configure("2") do |config|

  config.vagrant.plugins = "vagrant-disksize"

  (1..3).each do |i|
    config.vm.define "vm#{i}" do | node|
      node.vm.box = "ubuntu/bionic64"
      node.vm.hostname = "vm#{i}" 
      node.vm.network "private_network", ip: "10.0.0.2#{i}",
        auto_config: true,
        virtualbox__intnet: "priv-net"
      node.vm.network "private_network", ip: "#{$ip}#{i}" 
      node.vm.network "public_network"
      node.disksize.size = $disk_size 
    
      node.vm.provider "virtualbox" do |vb|
        vb.memory = $memory
        vb.cpus = $cpus
        vb.name = "vm#{i}"
      end
    end
  end

 config.vm.provision "file", source: "./ssh", destination: "/tmp/ssh"
 config.vm.provision "shell", inline: $script

end
