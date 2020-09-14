#!/bin/bash -xe

#Bootstrapping Kubernetes Cluster
if [ $HOSTNAME == "k8smaster" ]; then
    #initialize the cluster
    sudo kubeadm init --pod-network-cidr=10.244.0.0/16 \
        --apiserver-advertise-address=10.0.0.10| tee cluster.log
    mkdir -p ~vagrant/.kube ~/.kube
    sudo cp -i /etc/kubernetes/admin.conf ~vagrant/.kube/config
    sudo chown -R vagrant: ~vagrant/.kube
    sudo cp -i /etc/kubernetes/admin.conf  ~/.kube/config
    #The kubeadm init command should output a kubeadm join command containing a token and hash.
    join_cluster_command=$(tail -2 cluster.log)
    #Install network
    kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
    #join worker nodes to the cluster
    for node in k8snode1 k8snode2
    do
        sshpass -p "vagrant" ssh -o StrictHostKeyChecking=no \
            vagrant@$node "sudo $join_cluster_command"
    done
    sudo kubectl get nodes
else
    echo "Nothing to do here."
fi