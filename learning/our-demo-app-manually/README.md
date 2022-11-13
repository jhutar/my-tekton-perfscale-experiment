# Our demo app

Deploy and test the application is running:

    $ kubectl apply -f perfscale-demo-app-deploy.yaml
    $ curl http://localhost/app

Generate test data and connect to the pod with test code:

    $ kubectl -n perfscale-demo-app exec pod/perfscale-demo-app-556c65669-km5gn -- flask test-data
    $ kubectl -n perfscale-demo-app exec -it pod/testing-749cb7cb95-c75xb -- bash

And now in that "testing" pod, run the test:

    $ locust --locustfile testing.py --headless --users 20 --spawn-rate 10 -H http://perfscale-demo-service.perfscale-demo-app.svc:80 --run-time 30 --print-stats --only-summary
