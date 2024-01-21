import pandas as pd
from fastapi import HTTPException

from src.db import engine


def get_cellular(
    limit: int = 10,
    page: int = 1,
    mmc: list[str] | None = None,
    net: list[str] | None = None,
    area: list[str] | None = None,
    cell: list[str] | None = None,
    longitude: float | None = None,
    latitude: float | None = None,
    radius: float | None = None,
) -> list[dict]:
    query_params = "1 = 1"
    if mmc:
        query_params += f" AND mmc IN {tuple(mmc)}"
    if net:
        query_params += f" AND net IN {tuple(net)}"
    if area:
        query_params += f" AND area IN {tuple(area)}"
    if cell:
        query_params += f" AND cell_range IN {tuple(cell)}"
    if radius:
        if not longitude or not latitude:
            raise HTTPException(
                400, "longitude and latitude must be specified when radius is specified"
            )
        query_params += build_radius_filter(longitude, latitude, radius)
    else:
        if longitude:
            query_params += f" AND lon = {longitude}"
        if latitude:
            query_params += f" AND lat = {latitude}"
    query = f"""
        SELECT
            radio, mcc, net, area, cell, unit, lon, lat, cell_range,
            samples, changeable, created, updated, average_signal
        FROM
            cellular
        WHERE
            {query_params}
        LIMIT
            {limit}
        OFFSET
            {limit * (page - 1)}
    """
    df = pd.read_sql(query, con=engine)
    return df.to_dict(orient="records")


def build_radius_filter(x: float, y: float, radius: float) -> str:
    return f" AND ST_DWithin(geom, ST_SetSRID(ST_MakePoint({x}, {y}), 4326), {radius})"
