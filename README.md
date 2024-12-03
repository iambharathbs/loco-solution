# Multi stage docker build

Key Points

**Optimization:** Multi-stage builds for a lightweight production image.
**Scalability:** Configured HPA with CPU-based scaling to handle varying loads.
**Kubernetes Proficiency:** Defined deployment, service, and scaling policies with YAML files.
**Local Testing:** Used Minikube to replicate a production-like environment.

Python code creates simple web application that prints "Hello World"

**Build the docker image using the below command, **

_docker build -t iambharathbs/python-docker-app:latest . _

**Push to the docker registry using below command**

_docker push iambharathbs/python-docker-app:latest_

Start minikube on the local computer using the below command, 

_minikube start _

Apply yaml files 
kubectl apply *.yaml 

Check the status of deployment 
kubectl get deployment

Using kubectl port-forward to expose the service to a local port
_kubectl port-forward svc/python-docker-app-service 8080:80_

Access application using the below URL 
_http://localhost:8080_

Run the program generate_traffic.py to generate traffic




