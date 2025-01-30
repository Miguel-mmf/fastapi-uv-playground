from pydantic import BaseModel


class DateTimeModel(BaseModel):
    current_datetime: str
