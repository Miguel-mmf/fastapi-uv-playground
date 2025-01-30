from http import HTTPStatus

from fastapi import FastAPI

from app.api.endpoints import router
from app.schemas.schemas import MessageSchema
from app.settings.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

app.include_router(
    router=router,
    prefix="/api/v1",
    tags=["api"],
    responses={HTTPStatus.NOT_FOUND.value: {"description": "Not found"}},
)

@app.get("/", status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {"message": "Welcome to the FastAPI UV Datetime API"}
