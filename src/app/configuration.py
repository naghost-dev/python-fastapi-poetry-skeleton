from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APPLICATION: str = "app"

    API_VERSION: str = "v0"


settings = Settings()
