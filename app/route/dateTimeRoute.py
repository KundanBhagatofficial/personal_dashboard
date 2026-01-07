from fastapi import APIRouter
from app.source.dateTimeService import DateTimeService
from app.config import settings

router = APIRouter()
service = DateTimeService(settings.timezone)


@router.get("/datetime")
def get_datetime():
    return service.now()
