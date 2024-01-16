from unittest.mock import Mock

import pandas as pd
import pytest

from cellular import get_cellular


@pytest.fixture(autouse=True)
def run_around_tests(mocker: Mock):
    # Before
    mocker.patch("cellular.pd.read_sql", return_value=pd.DataFrame())
    yield
    # After


# @pytest.mark.asyncio
def test_cellular():
    get_cellular()
