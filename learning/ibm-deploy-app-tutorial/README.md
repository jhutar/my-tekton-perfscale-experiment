# IBM deploy app tutorial

See https://developer.ibm.com/tutorials/deploy-a-hello-world-application-on-kubernetes-using-tekton-pipelines/

First, build the app:

    $ git clone https://github.com/IBM/deploy-app-using-tekton-on-kubernetes.git
    # podman login -u="jhutar+tutorial_sampleapp_pusher" -p="<password>" quay.io
    # podman build .
    # podman tag <hash> quay.io/jhutar/tutorial-sampleapp:1.0
    # podman push quay.io/jhutar/tutorial-sampleapp:1.0
    $ kubectl apply -f ibm-example-deploy.yaml
    $ curl http://localhost/app

Now deploy with tekton pipeline

    $ kubectl apply -f deploy-app-using-tekton-on-kubernetes/tekton-pipeline/resources/git.yaml
    $ kubectl apply -f deploy-app-using-tekton-on-kubernetes/tekton-pipeline/task/build-src-code.yaml
    $ kubectl apply -f deploy-app-using-tekton-on-kubernetes/tekton-pipeline/task/deploy-to-cluster.yaml
    $ kubectl apply -f deploy-app-using-tekton-on-kubernetes/tekton-pipeline/pipeline/pipeline.yaml

Somewhere I lost both track and motivation :-)

    $ kubectl create secret generic ibm-cr-secret --type="kubernetes.io/basic-auth" --from-literal=username=my-deployer --from-literal=password=<APIKEY>
    $ kubectl annotate secret ibm-cr-secret tekton.dev/docker-0=<REGISTRY>

    $ kubectl create secret generic ibm-cr-secret --type="kubernetes.io/basic-auth" --from-literal=username=my-deployer --from-literal=password=LS0tL...
    $ kubectl apply -f deploy-app-using-tekton-on-kubernetes/tekton-pipeline/pipeline/service-account.yaml
