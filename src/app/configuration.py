from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APPLICATION: str = "app"

    API_VERSION: str = "v0"

    ENVIRONMENT: str = "local"


settings = Settings()
