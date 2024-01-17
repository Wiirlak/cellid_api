import io

import pandas as pd
from sqlalchemy import VARCHAR, Integer, Float
from geoalchemy2 import Geometry

from src.db import engine


def insert_cellular_data(file_data: bytes) -> None:
    df = pd.read_csv(io.BytesIO(file_data))
    df.rename(
        columns={"range": "cell_range", "averageSignal": "average_signal"}, inplace=True
    )
    df["geom"] = df.apply(lambda row: f"POINT({row['lon']} {row['lat']})", axis=1)
    print(df.head())
    print(f"size: {len(df)}")
    df.to_sql(
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
