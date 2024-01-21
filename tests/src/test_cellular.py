import pandas as pd
import pytest
from fastapi import HTTPException
from pytest_mock import MockFixture

from src.cellular import get_cellular


def test_cellular_run(mocker: MockFixture):
    mock_sql = mocker.patch("src.cellular.pd.read_sql", return_value=pd.DataFrame())
    get_cellular()
    assert mock_sql.call_count == 1


def test_cellular_query(mocker: MockFixture):
    mock_sql = mocker.patch("src.cellular.pd.read_sql", return_value=pd.DataFrame())
    get_cellular(
        limit=5,
        page=2,
        mmc=["1"],
        net=["1"],
        area=["1", "2"],
        cell=["1", "2"],
        longitude=1.0,
        latitude=2.0,
    )
    assert mock_sql.call_count == 1


def test_cellular_query_builder_radius(mocker: MockFixture):
    mock_sql = mocker.patch("src.cellular.pd.read_sql", return_value=pd.DataFrame())
    get_cellular(
        limit=5, page=2, cell=["1", "2"], longitude=1.0, latitude=2.0, radius=3.0
    )
    assert mock_sql.call_count == 1
    where_query = (
        mock_sql.call_args[0][0].split("WHERE")[1].strip().split("\n")[0].strip()
    )
    assert (
        where_query
        == "1 = 1 AND cell_range IN ('1', '2') AND ST_DWithin(geom, ST_SetSRID(ST_MakePoint(1.0, 2.0), 4326), 3.0)"
    )


def test_cellular_query_builder_radius_error(mocker: MockFixture):
    mock_sql = mocker.patch("src.cellular.pd.read_sql", return_value=pd.DataFrame())
    with pytest.raises(HTTPException):
        get_cellular(radius=3.0)
    assert mock_sql.call_count == 0
