from tier_backend.models.url import Url as ModelUrl
from sqlalchemy.exc import IntegrityError
from fastapi_sqlalchemy import db
import base62
import hashlib
import time
import re
from urllib.parse import urlparse, ParseResult
from tenacity import retry, retry_if_exception_type, stop_after_delay
import logging

logger = logging.getLogger(__name__)


def query_model() -> ModelUrl:
    return db.session.query(ModelUrl)


def rollback(callstate) -> None:
    url = callstate.kwargs.get("url")
    logger.error(f"Insertion of {url} failed.")
    db.session.rollback()


@retry(
    retry=retry_if_exception_type(IntegrityError),
    stop=stop_after_delay(5),
    before=rollback,
    reraise=True,
)
def create_and_insert_short_url(url: str) -> str:
    hash = get_current_time_hash()
    Url = ModelUrl(original_url=url, hash=hash)
    db.session.add(Url)
    db.session.commit()
    db.session.refresh(Url)
    return hash


def get_clean_url(url: str, only_internal: bool = False) -> str:
    parsed = urlparse(url)
    clean_url = parsed.geturl().strip(parsed.scheme).strip("://").strip("www.")
    if misses_dot(url, parsed.netloc) or (only_internal and not is_internal(clean_url)):
        raise ValueError("Invalid URL.")
    return clean_url


def misses_dot(url: str, netloc: str) -> bool:
    return not netloc and "." not in url


def is_internal(url: str) -> bool:
    return bool(re.search(r"\btier.app\/[a-zA-Z0-9]{7}\b", url))


def get_current_time_hash() -> str:
    current_time = str(time.time_ns()).encode()
    md5_hash = hashlib.md5(current_time).digest()
    long_hash = str(base62.encodebytes(md5_hash))
    short_hash = long_hash[:7]
    return short_hash
