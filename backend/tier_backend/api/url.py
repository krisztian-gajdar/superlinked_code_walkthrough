from fastapi import APIRouter, HTTPException
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)
from tier_backend.services.url import (
    get_clean_url,
    query_model,
    create_and_insert_short_url,
)
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/decode_url", response_model=dict)
async def decode_url(url: str):
    try:
        clean_url = get_clean_url(url=url, only_internal=True)
    except ValueError:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid URL."
        )

    hash = clean_url.split("/")[1]
    existing_result = query_model().filter_by(hash=hash).first()
    if not existing_result:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="URL does not exist."
        )
    return {"message": existing_result.original_url}


@router.post("/encode_url", response_model=dict)
async def encode_url(url: str):
    try:
        clean_url = get_clean_url(url=url)
    except ValueError:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid URL."
        )
    existing_result = query_model().filter_by(original_url=clean_url).first()
    if existing_result:
        hash = existing_result.hash
    else:
        hash = create_and_insert_short_url(url=clean_url)
    return {"message": f"tier.app/{hash}"}
