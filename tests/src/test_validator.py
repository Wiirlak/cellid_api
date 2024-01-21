import pandas as pd
import pytest
from fastapi import HTTPException

from src.validator import validate_csv


def test_validate_csv(cellular_fixtures: pd.DataFrame):
    validate_csv(cellular_fixtures)
    with pytest.raises(HTTPException):
        validate_csv(pd.DataFrame())
    with pytest.raises(HTTPException):
        validate_csv(pd.DataFrame([0], columns=["radio"]))
