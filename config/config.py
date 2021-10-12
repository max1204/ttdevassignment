from pydantic import BaseSettings

class Settings(BaseSettings):
    request_url:str

    class Config:
        env_file = ".env"

