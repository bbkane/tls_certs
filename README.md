# Notes

Using https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/

I created the root cert and used https://bbkane.github.io/2018/01/11/Fixing-HTTPS-CA-Cert-Issues.html to install it.

So I created the csr, key, and crt. But when I tried to run https://gist.github.com/dergachev/7028596 , it didn't work.

Trying https://notoriousno.blogspot.com/2017/11/simple-self-signed-tls-server-and.html

```
# rm password
openssl rsa -in host.key -out host_no_pass.key -passin pass:bbkane
# cat for PEM
cat host.crt host_no_pass.key > host.pem
# modify simple-https-server.py to use host.pem and serve on 0.0.0.0
```

client:

```
curl https://host:4443
```

And it works!

# TODO:

- reproduce this
- Make sequence diagram between client, host, and CA for provisioning and requesing HTTPS

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
