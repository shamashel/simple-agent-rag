from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(BaseSettings):
    OPENAI_API_KEY: str
    DOCUMENT_BATCH_COUNT: int = 1
    COMPANY_NAME: str = "Company XYZ"
    """Number of PDF documents to load at a time"""

    model_config = SettingsConfigDict(env_file=".env")

ENV = Environment()