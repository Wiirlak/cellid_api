import pandas as pd
from fastapi import HTTPException


COLUMN_NAMES = [
    "radio",
    "mcc",
    "net",
    "area",
    "cell",
    "unit",
    "lon",
    "lat",
    "range",
    "samples",
    "changeable",
    "created",
    "updated",
    "averageSignal",
]


def validate_csv(csv: pd.DataFrame) -> None:
    if csv.empty:
        raise HTTPException(400, "CSV file is empty")
    if not all(column in csv.columns for column in COLUMN_NAMES):
        raise HTTPException(
            400,
            "CSV file must have the following columns: "
            "radio, mcc, net, area, cell, unit, lon, lat, range, samples, changeable, created, updated, averageSignal",
        )
