# Multi stage docker build

**Python program "app.py" creates simple web application that prints "Hello World"**

Follow the below mentioned steps to build and deploy this applicaion on K8 cluster

1. Build the docker image using the below command,

    docker build -t iambharathbs/python-docker-app:latest . 

2. Push to the docker registry using below command

    docker push iambharathbs/python-docker-app:latest

3. Start minikube on the local computer using the below command, 

    minikube start

4. Apply yaml files 

    kubectl apply *.yaml 

5. Check the status of deployment and service, 

    kubectl get deployment
    kubectl get svc

7. Using kubectl port-forward to expose the service to a local port

    **kubectl port-forward svc/python-docker-app-service 8080:80**

8. Access application using the below URL 
    http://localhost:8080

9. Run the program **generate_traffic.py** to generate traffic




