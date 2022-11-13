# Tekton getting started guide

See https://tekton.dev/docs/getting-started/tasks/

    $ kubectl apply --filename hello-world.yaml
    $ kubectl apply --filename hello-world-run.yaml
    $ kubectl get taskrun hello-task-run
    $ kubectl logs --selector=tekton.dev/taskRun=hello-task-run

See https://tekton.dev/docs/getting-started/pipelines/

    $ kubectl apply --filename goodbye-world.yaml
    $ kubectl apply --filename hello-goodbye-pipeline.yaml
    $ kubectl apply --filename hello-goodbye-pipeline-run.yaml
    $ tkn pipelinerun logs hello-goodbye-run -f -n default

Or get the logs using:

    $ kubectl logs pod/hello-goodbye-run-hello-pod
    $ kubectl logs pod/hello-goodbye-run-goodbye-pod
