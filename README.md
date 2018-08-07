# Notes

Using https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/


# Usage

Please read the linked-above blog post for more detailed instructions. All
instructions are from the root repo location (in my case `~/Git/small_network`).

- Install Vagrant, VirtualBox, and Ansible (see the blog post for how I do this).

- Create the VMs:

```
vagrant up
```

- Create the local `ssh_config` file:

```
vagrant ssh-config > ssh_config
```

- Ping your new VMs with Ansible:

```
ansible all -m ping
```

- Run the test playbook:

```
ansible-playbook main.yml
```
