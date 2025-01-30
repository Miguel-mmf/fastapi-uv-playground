from fastapi import APIRouter
from app.services.datetime_service import get_current_datetime

router = APIRouter()


@router.get("/datetime")
def read_datetime():
    return {"current_datetime": get_current_datetime()}
