# Project folder for building FastAPI TODO app

This is a small project to pracice building an application with FastAPI, dockerising it and then potentially providing code to deploy and use it on the cloud. 

## Plan
- Build basic ToDo app functionality
- Dockerise it
- Create configs for a k8s cluster
- Create configs to deploy on Azure using terraform

## Usage

#### Directly using python
- Create a python env in fastapi_app
    - python3 -m venv <env_name>
- open environment 
    - source <env_name>/bin/activate
- install requirements
    - pip install -r requirements.txt
- uvicorn main:app --port=<PORT_NUMBER> 

#### Docker
- cd into fastapi_app

- docker build -t <docker_image_name> .
- docker run  -p 8001:8001 <docker_image_name>


#### Docker Compose
- docker compose up -d --build
    - include --build if you want to build docker containers as well 

- docker compose down
    - to stop the containers     


#### Run unittests
- python3 -m unittest discover



## Requirements
### Functional
- Users can upload items to the todo
- Users can get a list of items from the todo
- Users can mark a todo item as complete

### Non Functional
- Should have 99.9 availability
- Prioritise uniqueness

### Specifications
- FastAPI endpoint with following location
    - GET - to get a list of items
    - GET {item_id} - to get a specific item by id
    - POST - to put an item on the list
    - POST {complete} - to mark item as complete 
    - DELETE - remove a item from the list
- Pydantic model Items to contain the items

- Try catch blocks and effective responses should be given as repsonses from the model. 


## Tests
- Unit tests are run on this to ensure that everything is running correctly

- Run tests using the following command
    - cd fastapi_app/src/ 
    - python3 -m unittest discover


#### Running kubernetes cluster to host
- N.B - you will need cluster provisioned
    - For simplicity can use minikube

##### RUn following commands
- minikube start 
    - Initialises the cluster
    - For different providers you will need to configure access

-  minikube image load fastapi_todo_app:1.0.0
    - ensures image is loaded into minikube docker environmnet

- kubectl apply -f todo-deployment.yaml
    - applies the deployment
    - can edit and reapply to rollout new changes 

- kubectl apply -f load-balancer-service.yaml
    - creates load balancer service 

- kubectl get all 
    - lists all created deployments and services 
    - use to check all created properlys

- minikube service fastapi-todo-api-loadbalancer --url
    - return the url back for the load balancer which allows you to route traffic into the server
    - you will need to use this to access the app

- minikube delete 
    - these will delete everything for you 


