# My Tekton perf&scale experiment

My goal is to create a Tekton pipeline that deploys simple webapp, runs a performance test, based on historical results of a same test it decides on a test result and returns a result.

## Our demo app

Remove mentions about volumes in PostgreSQL pod and:

    $ kubectl apply -f ../perfscale-demo-app/deploy.yaml
    $ kubectl -n perfscale-demo-app apply -f perfcale-demo-app-ingress.yaml
    $ kubectl -n perfscale-demo-app apply -f perfcale-demo-app-ingress.yaml
    $ curl http://localhost/app

Generate test data and start the test:

    $ kubectl -n perfscale-demo-app exec pod/perfscale-demo-app-556c65669-km5gn -- flask test-data
    $ kubectl -n perfscale-demo-app exec -it pod/testing-749cb7cb95-c75xb -- bash
