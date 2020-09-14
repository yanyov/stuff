#!/bin/bash -xe

#enable password ssh login
sudo sed -i 's/PasswordAuthentication no/#PasswordAuthentication no/g' /etc/ssh/sshd_config
sudo systemctl restart sshd

#Prevent question “Restart services during package upgrades without asking?”
echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections

#install docker-ce and sshpass
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    sshpass \
    bash-completion \
    nfs-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
sudo apt-get update
DOCKER_VERSION="18.06.2~ce~3-0~ubuntu"
sudo apt-get install -y docker-ce=$DOCKER_VERSION

sudo apt-mark hold docker-ce

# Setup docker daemon
cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF

mkdir -p /etc/systemd/system/docker.service.d

# Restart docker
systemctl daemon-reload
systemctl restart docker

#install Kubeadm, Kubelet, and Kubectl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo deb https://apt.kubernetes.io/ kubernetes-xenial main >> /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
KUBE_VERSION="1.16.3-00"
sudo apt-get install -y \
    kubelet=$KUBE_VERSION \
    kubeadm=$KUBE_VERSION \
    kubectl=$KUBE_VERSION
    
sudo apt-mark hold kubelet kubeadm kubectl

modprobe --all br_netfilter ip_vs ip_vs_rr ip_vs_wrr ip_vs_sh nf_conntrack_ipv4

#modules to load at boot
echo >> /etc/modules << EOF
br_netfilter 
ip_vs ip_vs_rr 
ip_vs_wrr 
ip_vs_sh 
nf_conntrack_ipv4 
EOF

#add ip addresses to /etc/hosts
echo "192.168.100.10    k8smaster" >> /etc/hosts
echo "192.168.100.11    k8snode1" >> /etc/hosts
echo "192.168.100.12    k8snode2" >> /etc/hosts

#add comand-line completion for kubectl
echo "source <(kubectl completion bash)" >> /etc/bash.bashrc

#set kernel parameters
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p