import io

import pandas as pd
from fastapi import APIRouter, UploadFile, Query, HTTPException

from src.cellular import get_cellular
from src.populate import insert_cellular_data
from src.validator import validate_csv

router = APIRouter()


@router.post("/populate")
async def populate(file: UploadFile) -> dict:
    try:
        csv = pd.read_csv(io.BytesIO(await file.read()))
    except Exception:
        raise HTTPException(400, "Error parsing CSV file")
    validate_csv(csv)
    insert_cellular_data(csv)
    return {"status": "OK"}


@router.get("/cellular")
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
