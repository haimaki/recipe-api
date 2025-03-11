# Recipe API

## Description
A simple backend service for retrieving recipes, adjusting portion sizes and converting units.

## Installation
### 1. Clone the repository
```
git clone https://github.com/haimaki/recipe-backend.git
cd recipe-backend
```

### 2. Install dependencies
```
pip install -r .\requirements\local.txt
```


### 3. Run the server
```
fastapi run .\interfaces\api.py
```


## Running Tests
To run tests, use:
```
pytest
```

To check test coverage, use:
```
coverage run -m pytrst
coverage report
```


## API Documentation
Documentation of methods and models can be found at:
```http://0.0.0.0:8000/docs``` after running the server.