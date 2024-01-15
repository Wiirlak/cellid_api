from fastapi import APIRouter, UploadFile

from src.cellular import get_cellular
from src.scraper import scrape_data

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.post("/populate")
async def populate(file: UploadFile) -> dict:
    d = await file.read()
    print(d)
    status = scrape_data()
    return {"status": status}


@router.get("/cellular")
async def cellular(
    limit: int = 10,
    page: int = 1,
    mmc: list[str] | None = None,
    net: list[str] | None = None,
    area: list[str] | None = None,
    cell: list[str] | None = None,
) -> dict:
    return get_cellular(limit, page, mmc, net, area, cell)
