import io

import pandas as pd

from src.db import engine


def insert_cellular_data(file_data: bytes) -> None:
    df = pd.read_csv(io.BytesIO(file_data))
    df.rename(
        columns={"range": "cell_range", "averageSignal": "average_signal"}, inplace=True
    )
    print(df.head())
    print(f"size: {len(df)}")
    df.to_sql("cellular", con=engine, if_exists="replace", chunksize=1000, index=False)
