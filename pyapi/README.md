# FASTAPI Aplication with Crud methods
This is a sample application that reads, write, delete and get information from a database.
FastAPI is a Python class that provides all the functionality for your API
Here the app variable will be an instance of the class FastAPI. This will be the main point of interaction to create your API.

This app is the same one you referred to above in the command to run the live server with uvicorn :
Use gunicorn to bring the python application ready for production.

This repo also includes the dockerfiles to build the containers for each portion of the app, then it also would include the kubernetes .yaml files to deploy the application to kubernetes cluster.

The solution for the problem in the test is this one:
# For testing locally the application:
Create a virtual environment with: 
python3 -m venv [env_name] && source env_name/bin/activate
or if you like me use your already setup mkvirtualenv command.
workon env_name

then install the required libraries:
pip install fastapi uvicorn sqlalchemy psycopg2

# For testing gunicorn application, with allowing live changes with reload, execute:
```uvicorn main:app --reload --port=8000 --host=0.0.0.0```
Then you can test the app at: http://localhost:8000
if apply any change to the app.py it gets automatically applied by the reload
note: if you are having problems with your virtualenv to run uvicorn, you can try execute
```python -m uvicorn main:app --reload --port=8000 --host=0.0.0.0```

We can check the interactive documentation of the application, in the browser go to: http://localhost:8000/docs, and the read document: http://localhost:8000/redoc

# To test locally you cn bring up the postgress database with
```docker compose -f postgres.compose.yaml up -d```
Then start the api:
```python -m uvicorn main:app --reload --port=8000 --host=0.0.0.0```

Now you can test the API operations against the database.

# To build the docker image directly:
```docker build -f fastapipg.dockerfile -t zelfick/fastapipg .```

# To push the image
```docker push zelfick/fastapipg:latest```

# Testing the api and db 
 In the project directory (pyapi), execute:
```
docker compose -f docker.compose.yaml up -d
```
At this point, the application should be running at [http://localhost:8000/](http://localhost:8000/). To stop the applicationa and remove created volume, you can run:
```
docker compose -f docker.compose.yaml down -v
```
To restart or rebuild the application, you can run:
```
docker compose -f docker.compose.yaml up --build
```

# Kubernetes base files
They are placed in pyapi/k8s folder, and there are files to create the namespace, all the objects required to postgress and the objects requires for fastapi.

# To deploy the namespace
```
kubectl apply -f namespace.yaml
```

# To deploy all the resources from fastapi/ and postgres/ you can execute: kubectl apply -f {folder_name}
```
kubectl apply -f postgres
kubectl apply -f fastapi
```
