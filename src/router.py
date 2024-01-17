from fastapi import APIRouter, UploadFile, Query

from src.cellular import get_cellular
from src.populate import insert_cellular_data

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.post("/populate")
async def populate(file: UploadFile) -> dict:
    d = await file.read()
    insert_cellular_data(d)
    return {"status": "OK"}


@router.get("/cellular/")
async def cellular(
    limit: int = Query(10),
    page: int = Query(1),
    mmc: list[str] | None = Query(None),
    net: list[str] | None = Query(None),
    area: list[str] | None = Query(None),
    cell: list[str] | None = Query(None),
    longitude: float | None = Query(None, ge=-180, le=180),
    latitude: float | None = Query(None, ge=-90, le=90),
    radius: float | None = Query(None, ge=0),
) -> list[dict]:
    return get_cellular(limit, page, mmc, net, area, cell, longitude, latitude, radius)
