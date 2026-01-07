from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Dashboard"
    env: str = "dev"
    timezone: str = "Asia/Kolkata"


settings = Settings()
