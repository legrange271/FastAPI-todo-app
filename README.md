# Project folder for building FastAPI TODO app

This is a small project to pracice building an application with FastAPI, dockerising it and then potentially providing code to deploy and use it on the cloud. 

## Plan
- Build basic ToDo app functionality
- Dockerise it
- Create configs for a k8s cluster
- Create configs to deploy on Azure using terraform

## Usage

#### Directly using python
- Create a python env
    - python3 -m venv <env_name>
- open environment 
    - source <env_name>/bin/activate
- install requirements
    - pip install -r requirements.txt
- uvicorn main:app --port=<PORT_NUMBER> 

#### Docker
- docker build -t <docker_image_name> .
- docker run  -p 8001:8001 <docker_image_name>


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
    - python3 -m unittest discover
