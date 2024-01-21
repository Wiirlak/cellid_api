import pandas as pd
from fastapi import HTTPException
from sqlalchemy import VARCHAR, Integer, Float
from geoalchemy2 import Geometry

from src.db import engine


def insert_cellular_data(file_data: pd.DataFrame) -> None:
    file_data.rename(
        columns={"range": "cell_range", "averageSignal": "average_signal"}, inplace=True
    )
    file_data["geom"] = file_data.apply(
        lambda row: f"POINT({row['lon']} {row['lat']})", axis=1
    )
    print(f"size: {len(file_data)}")
    try:
        file_data.to_sql(
            "cellular",
            con=engine,
            if_exists="replace",
            chunksize=1000,
            index=False,
            dtype={
                "radio": VARCHAR,
                "mcc": Integer,
                "net": Integer,
                "area": Integer,
                "cell": Integer,
                "unit": Integer,
                "lon": Float,
                "lat": Float,
                "cell_range": Integer,
                "samples": Integer,
                "changeable": Integer,
                "created": Integer,
                "updated": Integer,
                "average_signal": Integer,
                "geom": Geometry("POINT", srid=4326),
            },
        )
    except Exception as e:
        raise HTTPException(400, str(e))
