import pandas as pd
import pytest
from fastapi import HTTPException
from pytest_mock import MockFixture

from src.populate import insert_cellular_data


def test_populate_run(cellular_fixtures: pd.DataFrame, mocker: MockFixture):
    mock_insert = mocker.patch("src.populate.pd.DataFrame.to_sql", return_value=None)
    insert_cellular_data(cellular_fixtures)
    assert mock_insert.call_count == 1


def test_populate_run_fail(cellular_fixtures: pd.DataFrame):
    with pytest.raises(Exception):
        insert_cellular_data(pd.DataFrame())
    with pytest.raises(HTTPException):
        insert_cellular_data(cellular_fixtures)
