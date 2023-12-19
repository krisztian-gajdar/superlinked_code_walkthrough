from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from tier_backend.core.config import Settings
import logging
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)
settings = Settings()
Base = declarative_base()


def init_db():
    engine = create_engine(settings.db_url)
    db_session = scoped_session(
        sessionmaker(bind=engine, autocommit=False, autoflush=False)
    )
    Base.metadata.create_all(bind=engine)
    db_session.commit()
    logger.info("Database initialized.")
