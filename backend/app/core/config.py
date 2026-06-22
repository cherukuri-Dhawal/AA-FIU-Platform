from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AA FIU Platform"

    DIGIO_CLIENT_ID: str = ""
    DIGIO_CLIENT_SECRET: str = ""

    DATABASE_URL: str = "sqlite:///./aa_fiu.db"

    class Config:
        env_file = ".env"


settings = Settings()