# Recipe API

## Description
A simple backend service for retrieving recipes, adjusting portion sizes and converting units.

## Requirements
This project requires a PostgreSQL server and and a connection string to be set as `POSTGRES_CONNECTION_STRING`

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

### 4. Create database tables

```
python create_tables.py
```


### 3. Run the server
```
fastapi run .\interfaces\api.py
```

## Requirements
- PostgreSQL server

## API Endpoints
### List Recipes
Endpoint: `GET /recipes/`

Example Response
```
[
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "title": "Spaghetti Bolognese",
    },
    {
        "id": "a2d0acf9-192c-461f-bb0d-d871a52c5b3a",
        "title": "Chicken Curry",
    }
]
```

### Get Recipe Ingredient List

Endpoint: `GET /recipes/{recipe_id}/ingredients`

Example Response
```
[
    {
        "name": "Spaghetti",
        "quantity": 450.0,
        "unit": "g"
    },
    {
        "name": "Tomato Sauce",
        "quantity": 750.0,
        "unit": "ml"
    }
]
```

## API Documentation
Documentation of methods and models can be found at:
```http://0.0.0.0:8000/docs``` after running the server.


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

## Assumptions

As no restrictions on library usage were given, Pint has been used for unit conversion.
Ingredients have been separated into an `Ingredient` and `RecipeIngredient` for extensibility.