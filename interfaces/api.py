from fastapi import FastAPI

from interfaces.rest_api.routers.recipe import router as recipe_router

app = FastAPI()

app.include_router(recipe_router, tags=["recipe"], prefix="/recipe")
