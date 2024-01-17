from unittest.mock import Mock

import pandas as pd
import pytest

from fictures.cellular_fixture import cellular_fixtures
from src.cellular import get_cellular


@pytest.fixture(autouse=True)
def run_around_tests(mocker: Mock):
    # Before
    mocker.patch("src.cellular.pd.read_sql", return_value=pd.DataFrame())
    yield
    # After


def test_cellular(mocker: Mock):
    db = mocker.patch("src.cellular.pd.read_sql", return_value=pd.DataFrame())
    get_cellular()
    assert db.call_count == 1


def test_cellular_paginate(mocker: Mock):
    mocker.patch("src.cellular.pd.read_sql", return_value=cellular_fixtures())
    get_cellular(limit=5, page=2)
