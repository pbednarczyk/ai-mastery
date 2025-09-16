from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ai-app-template"
    app_env: str = "local"
    app_version: str = "0.1.0"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # <-- ważne: ignoruj nieznane zmienne
    )


settings = Settings()
