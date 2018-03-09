This is a starter repo for using Vagrant + Ansible in a fairly clean way.
I've created [a blog
post](https://bbkane.github.io/2017/10/27/An-Isolated-and-Reproducible-Ansible-and-Vagrant-Setup.html)
for this repo to follow.

# Goals

- Be cleanly installable/uninstallable. If everyone moves to containers, I want to be able to cleanly get rid of this.
- Be reproducible on any computer.

# Usage

Please read the linked-above blog post for more detailed instructions.

- Install Vagrant, VirtualBox, and Ansible (see the blog post for how I do this).
- Create the local `ssh_config` file:

```
vagrant ssh-config > ssh_config
```

- Ping your new VMs with Ansible

```
ansible all -m ping
```
