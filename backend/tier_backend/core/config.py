from pydantic import BaseSettings


class Settings(BaseSettings):
    title: str = 'Tier Backend'
    db_url: str = 'sqlite:///local.db'
