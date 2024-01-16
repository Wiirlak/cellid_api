import pandas as pd

from src.db import engine


def get_cellular(
    limit: int = 10,
    page: int = 1,
    mmc: list[str] | None = None,
    net: list[str] | None = None,
    area: list[str] | None = None,
    cell: list[str] | None = None,
    lon_min: float | None = None,
    lon_max: float | None = None,
    lat_min: float | None = None,
    lat_max: float | None = None,
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
    if lon_min:
        query_params += f" AND lon >= {lon_min}"
    if lon_max:
        query_params += f" AND lon <= {lon_max}"
    if lat_min:
        query_params += f" AND lat >= {lat_min}"
    if lat_max:
        query_params += f" AND lat <= {lat_max}"
    if radius:
        if not lon_min or not lat_min:
            raise ValueError(
                "lon_min and lat_min must be specified when radius is specified"
            )
        raise NotImplementedError("radius is not implemented")
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
