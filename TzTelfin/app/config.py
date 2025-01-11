from pydantic_settings import BaseSettings


class Settings(BaseSettings): 

    API_URL: str
    HEADER: str
    KEY: str

    class Config:
        env_file = ".env"

settings = Settings() 

HEADERS = {
    settings.HEADER: settings.KEY
}


