from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(BaseSettings):
    COMPANY_NAME: str
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str = "" # Optional, only if you want to try google search
    DOCUMENT_BATCH_COUNT: int = 1
    """Number of PDF documents to load at a time"""

    model_config = SettingsConfigDict(env_file=".env")

ENV = Environment()