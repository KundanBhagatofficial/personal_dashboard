from fastapi import FastAPI
from app.route.dateTimeRoute import router as DateTimeService


app = FastAPI()
app.include_router(DateTimeService)


@app.get("/health")
def show():
    return {"system": "ok"}
