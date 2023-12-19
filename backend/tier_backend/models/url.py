from sqlalchemy import Column, String
from tier_backend.db.base import Base


class Url(Base):
    __tablename__ = "url"
    original_url = Column(String(2048), primary_key=True, index=True)
    hash = Column(String(7), unique=True)
