# Provisioning homewerk

This provisions a Virtualbox VM using Vagrant and ansible

Vagrantfile already has the Ansible provisioner configured, we just need to add more tasks

# Steps

This are the steps taken by the Ansible play and reasoning

### Pre-reqs

1. Add the runit yum repo using Ansible. Its a bad idea to add 3rd party yum repos and even worse to use a 3rd party script. Looks like their script even installs some rpm's, thats no a no go. We add the repo using pure Ansible. If we are already using Ansible, we should manage everything with it end-to-end. In a production system we would mirror the repo or put the rpm into our own private yum repo.
2. for security purposes, update the OS. We want latest packages
3. Install the rpms that we need, this includes nginx and runit

### App & runit

1. Create an app user and group
2. create app dir
3. create runit service dir
4. extract `application.zip` to /opt
5. patch the run script to exec as non-root user
6. symlink run script to runit service
7. runit starts it automatically

### nginx

1. create an ssl  group, add nginx user to the ssl group
2. Place the cert and key into `/etc/nginx/ssl`
3. Set permissions on dir 0710 and files 0640, owned by root and only readable by ssl group
4. Copy nginx conf
5. start nginx service. In a more prod setup we would create an Ansible service handler
