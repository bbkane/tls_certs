# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  # set settings common to all VMs
  config.vm.box = 'centos/7'
  # Disable the default synced folder because it's too much trouble to set up
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.synced_folder '.', '/home/vagrant/sync', disabled: true

  # Don't check the host key
  config.ssh.verify_host_key = false

  # Add some VirtualBox specific settings
  config.vm.provider 'virtualbox' do |vb|
    vb.gui = true
    vb.customize ['modifyvm', :id, '--clipboard', 'bidirectional']
  end

  # Create and set VM specific settings

  # I'm setting some static IPs so the nodes can ping each other. These might
  # conflict with something else on your network, and if so, change them.
  config.vm.define :node1 do |node1|
    node1.vm.hostname = 'node1'
    node1.vm.network 'private_network', ip: '192.168.33.10'
  end

  config.vm.define :node2 do |node2|
    node2.vm.hostname = 'node2'
    node2.vm.network 'private_network', ip: '192.168.33.11'
  end
end
