# fastapi-Test-ORBIDI

In this case I have a system of two CRUD services of Locations and Categories which are related.

##  Description

This is a basic python api setup using the FastAPI framework. It is deployable to the cloud out of the box without much configuration or changes needed (if any at all).

###  Directory Structure
```
ORBIDI BACKEND
├── .env
│   .gitignore
│   docker-compose.yaml
│   Dockerfile
│   README.md
│
└───app
    │   main.py
    │   req.http
    │   __init__.py
    │
    ├───api
    │   │   __init__.py
    │   │
    │   ├───database
    │   │   │   db_operations.py
    │   │   │   __init__.py
    │   │   │
    │   │   └───__pycache__
    │   │           db_operations.cpython-310.pyc
    │   │           __init__.cpython-310.pyc
    │   │
    │   ├───endpoints
    │   │   │   category.py
    │   │   │   locations.py
    │   │   │   __init__.py
    │   │   │
    │   │   └───__pycache__
    │   │           category.cpython-310.pyc
    │   │           locations.cpython-310.pyc
    │   │           __init__.cpython-310.pyc
    │   │
    │   ├───schemas
    │   │   │   category.py
    │   │   │   locations.py
    │   │   │   __init__.py
    │   │   │   
    │   │   └───__pycache__
    │   │           category.cpython-310.pyc
    │   │           locations.cpython-310.pyc
    │   │           __init__.cpython-310.pyc
    │   │
    │   ├───services
    │   │   │   services.py
    │   │   │   
    │   │   └───__pycache__
    │   │           services.cpython-310.pyc
    │   │
    │   └───__pycache__
    │           __init__.cpython-310.pyc
    │
    ├───core
    │   │   application.py
    │   │   config.py
    │   │   database.py
    │   │   logger.py
    │   │   models.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           application.cpython-310.pyc
    │           config.cpython-310.pyc
    │           database.cpython-310.pyc
    │           logger.cpython-310.pyc
    │           models.cpython-310.pyc
    │           __init__.cpython-310.pyc
    │
    └───__pycache__
            main.cpython-310.pyc
###  Features

-  Docker compose

-  python 10.8

-  MySql

-  /app/req.http  documentation to consume services

-  http://127.0.0.1:8000/docs  Seagger

##  Getting Started

Getting started developing with this template is pretty simple using docker and docker-compose.

```shell script
# Clone the repository
git clone https://github.com/JhonFac/backen_ordibi.git

# cd into project root
cd backen_ordibi/app

# launch the project in three ways

- python app/main.py

- uvicorn main:api --reload

- docker-compose up
```

Afterwards, the project will be live at [http://localhost:8000](http://localhost:8000).

## Documentation

FastAPI automatically generates documentation based on the specification of the endpoints you have written. You can find the docs at [http://localhost:8000/docs](http://localhost:8000/docs).


