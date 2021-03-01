# Practice k8S Bootcamp DevOps

Final project for the K8s module to connect a microservice with an simple pyton(flask) app which reads information from a Mongo database and shows it on the browser in json format. I will be implementing different solutions using docker, K8s, Helm, and Istio.

## Using Docker
### Build the application 🔧
To clone this project just press on the clone button on the upper right side or use the  git clone git@gitlab.keepcoding.io:JesusFernandez86/practica-final-docker-k8s.git command. Once downloaded use the build command to build the flask app image
```shell
docker build -t latalavera/flask-app:1.0 .
```
Or also you can just download the existing image from Dockerhub by using:
```shell
docker pull latalavera/flask-app:1.0
```

### Run the container 🚀
To create a container from the image
```shell
docker run --name <my-container-name> -d -p 5000:5000 latalavera/webapp:1.0
```
In order to run the app and have acces to the database, you will need to run the flask-app along with its MongoDB container, docker-compose.yml is configured to do that already. If you need to change the ports in which the containers are going to be working you can do so in the .env file. Also if you need to change some settings from the database container such as database, username, pasword etc... you can do so by modifying or adding environmnet variables oon the db-env-vars.env file. Once the setup is ready you just need to execute the
```shell
docker-compose up
```
The containers should be running after a minute, to make sure, just go in your browser to http://localhost:5000 and if you see a message the app is running. To check connectivity with MongoDB container go to http://localhost:5000/cars and check if you get the list of cars

## Using K8s
### Create secret
First of all you will need to generate a secret with the root username and password, you can do that by using the following command (bare in mind user and password must be stored encoded in base64) *make sure the secret is called mongo-credentials*:
```shell
MONG_USER=<mymongouser>
MONGO_PASSWORD=<mysecretpassword>
NAMESPACE=flask-app
kubectl -n $NAMESPACE create secret generic mongo-credentials --from-literal=MONGO_INITDB_ROOT_PASSWORD=$MONGO_PASSWORD--from-literal=MONGO_INITDB_ROOT_USERNAME=$MONG_USER
```

### Create an Nginx-Ingres-controller
```shell
~$ kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $(gcloud config get-value account)
~$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.44.0/deploy/static/provider/cloud/deploy.yaml
```
Then run the following command
```shell
kubectl get svc -n ingress-nginx
```
and get the external ip address and copy it to the host field in your ingress.yaml, adding <yourip>.nip.io at the end, then update your ingress and paste that addres in your browser to visit the website externally. Further information about ip address allowd can be found here https://nip.io/

### Install Prometheus
All the required files to install prometheus are within the prometheus folder. All the setup has been done so by using the following command you can isntall all the required objects:
```shell
kubectl apply -f prometheus
```
Then you can check if prometheus by visiting your localhost:9090, but before you need to forward the port 9090, using in your terminal:
```shell
kubectl port-forward service/prometheus 9090 -n monitoring
```
Once you are in the browser click on status -> targets to see the pods which are being tracked.

## Using Helm
First of all change to flask-app namespace and upgrade the chart dependencies to download the mongodb from Bitnami by using:
```shell
ns flask-app
helm upgrade <release_name> 
```
Then install the chart by navigating to /charts/flask-app and running:
```shell
helm install -n flask-app <release_name> . 
```

### Using Istio
To install Istio execute the following commands:
```shell
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.9.0 sh -
export PATH="$PATH:<yourpath>"
istioctl install --set profile=demo
kubectl label ns istio istio-injection=enabled 
```
Then navigate to the canary-istio folder and execute the apply command on the folder:
```shell
kubectl apply -f .\canary-istio\   
```
Then check your external ip by running:
```shell
kubectl -n istio-system  get svc
```
and check the istio-ingressgateway external ip column, copy and paste that addres in your browser and reload a few times to see how the home page welcome message changes

## Built with 🛠️
* [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) - Kubernetes CLI tool
* [Docker Desktop](https://www.docker.com/products/docker-desktop) - Docker tool for Mac and Windows systems
* [Helm](https://helm.sh/) - Package manager for Kubernetes

## Author ✒️

* **Jesus Fernandez Arroyo** -(https://www.linkedin.com/in/jesus-fernandez-b3a969b0/)