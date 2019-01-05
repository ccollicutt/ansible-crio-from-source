# cri-o from source

This will deploy [cri-o](https://cri-o.io/) from source on Ubuntu Xenial. There is a [ppa](https://launchpad.net/~projectatomic/+archive/ubuntu/ppa) that has packages for cri-o, but sometimes it does not have the latest cri-o available. (Such as right now.) But it may have the latest now, so it might be best to check there first before using this role.

In order to build and use cri-o with Kubernetes a few things are required, and this role does most of them:

* Installs go
* Installs runc - This can be disabled by setting `crio_install_runc: false` in defaults.
* Sets up /etc/default/kubelet to use cri-o - This can be disabled be setting `crio_manage_kubelet_extra_args: false` in defaults
* Installs cri-o from source - make.tools, make, make.install, make.config
* Installs a few configuration files to enable cri-o

## Versions

See the various versions in the `defaults/main.yml` file.
