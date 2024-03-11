from fastapi import FastAPI
from routes import router

# Creating an instance of the FastAPI application
app = FastAPI()

# Including the router defined in the routes module
# This router contains the API endpoints
app.include_router(router)
