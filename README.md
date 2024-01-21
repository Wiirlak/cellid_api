# CellID API

## Overview
This is a REST API for the CellID project. It is built using Python and Flask.

## Prerequisites
- Python
- Docker
- Docker Compose

Copy the .env.example file to .env and fill in the values according to your environment.

## Installation

### Docker
```bash
git clone https://github.com/Wiirlak/cellid_api.git
cd cellid_api
docker-compose up
```

### Local
You should have a PostgreSQL database running on port 5432. You can use the docker-compose.yml file to run a PostgreSQL database in a container.
```bash
git clone
cd cellid_api
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Usage
The API documentation is available at http://localhost:8000/docs

## TESTING
Tests are written using pytest. To run the tests, run the following command:
```bash
pytest --cov=app tests/

# To generate a coverage report
pytest --cov=app --cov-report html tests/

# To run a specific test
pytest tests/test_users.py::test_get_user
```