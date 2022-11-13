# Setup `kind` and Tekton

## Install tools

See https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries

    $ wget -O /home/jhutar/bin/kind https://github.com/kubernetes-sigs/kind/releases/download/v0.17.0/kind-linux-amd64
    $ chmod +x /home/jhutar/bin/kind

See https://tekton.dev/docs/cli/

    # dnf copr enable chmouel/tektoncd-cli
    # dnf install tektoncd-cli


## Deploy `kind` cluster

    # mkdir /var/tmp/kind-cluster/
    # /home/jhutar/bin/kind delete cluster
    # /home/jhutar/bin/kind create cluster --config kind-cluster.yaml
    # /home/jhutar/bin/kind export kubeconfig --kubeconfig /home/jhutar/.kube/config


## Create user for deployment pipeline

See https://medium.com/@lionelvillard/creating-users-in-kind-cluster-6c5ee35db3fe

    # kind get kubeconfig
    $ echo ... | base64 -d > kind.csr
    $ openssl x509 -in kind.csr -noout -text | grep Subject:
        Subject: O = system:masters, CN = kubernetes-admin
    $ kubectl -n kube-system get clusterrolebindings.rbac.authorization.k8s.io cluster-admin -o yaml
    $ kubectl -n kube-system get clusterrole.rbac.authorization.k8s.io cluster-admin -o yaml

    # podman cp kind-control-plane:/etc/kubernetes/pki/ca.crt /home/jhutar/Checkouts/my-tekton-perfscale-experiment/
    # podman cp kind-control-plane:/etc/kubernetes/pki/ca.key /home/jhutar/Checkouts/my-tekton-perfscale-experiment/
    # chmod 644 ca.crt ca.key
    $ openssl genrsa -out my-deployer.key 2048
    $ openssl req -new -key my-deployer.key -out my-deployer.csr -subj "/CN=my-deployer/O=tenant1"
    $ openssl x509 -req -in my-deployer.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out my-deployer.crt -days 360

    $ cat ca.crt | base64 --wrap=0
    $ cat my-deployer.crt | base64 --wrap=0
    $ cat my-deployer.key | base64 --wrap=0
    $ kubectl --kubeconfig=config --cluster=kind-kind --context=my-deployer --user=my-deployer get namespace
    ...does not work
    $ kubectl apply -f my-deployer-config.yaml
    $ kubectl --kubeconfig=config --cluster=kind-kind --context=my-deployer --user=my-deployer get namespace


## Or this way?

See https://www.tutorialworks.com/openshift-cluster-admin/

    $ htpasswd -cBb htpasswd mydeployer redhat
    $ kubectl create secret generic htpasswd --from-file=htpasswd -n kube-system


## Install Tekton

    $ kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
    $ kubectl -n tekton-pipelines get pods


## Configure persistent storage - TODO

    $ kubectl get StorageClass
    $ kubectl get StorageClass/standard -o yaml

    $ kubectl get -A ConfigMap
    $ kubectl -n tekton-pipelines edit ConfigMap/config-artifact-pvc
    data:
      size: 1GiB
      storageClassName: standard


## Configure ingress - TODO

See https://kind.sigs.k8s.io/docs/user/ingress

    $ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

Now test it

    $ kubectl apply -f using-ingress.yaml
    $ curl http://localhost/foo
    $ curl http://localhost/bar
    $ kubectl delete -f using-ingress.yaml
