# My Tekton perf&scale experiment

My goal is to create a Tekton pipeline that deploys simple webapp, runs a performance test, based on historical results of a same test it decides on a test result and returns a result.

## Let's go

    tkn hub install task git-clone
    tkn hub install task kubernetes-actions
    kubectl apply --filename pipeline.yaml
    kubectl apply --filename sa.yaml
    kubectl create --filename pipeline-run.yaml

To re-run a pipeline run, just do this:

    kubectl create --filename pipeline-run.yaml
    tkn pipelinerun logs --follow --last
