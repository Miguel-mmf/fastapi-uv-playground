from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    PROJECT_VERSION: str


settings = Settings()
