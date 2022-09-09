from src.db import init_models
from src.schemas import User
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_models()


@app.post("/login/", response_model=User)
async def root(user: User):

    return {"message": "Hello World"}



def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
