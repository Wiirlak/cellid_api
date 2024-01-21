import pandas as pd
from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from main import app

client = TestClient(app)


def test_read_cellular(cellular_fixtures: pd.DataFrame, mocker: MockFixture):
    mocker.patch("src.cellular.pd.read_sql", return_value=cellular_fixtures)
    response = client.get("/api/v1/cellular")
    assert response.status_code == 200
    assert len(response.json()) == len(cellular_fixtures)


def test_post_populate(cellular_fixtures: pd.DataFrame, mocker: MockFixture):
    mocker.patch("src.populate.pd.DataFrame.to_sql", return_value=None)
    response = client.post(
        "/api/v1/populate",
        files={"file": ("test.csv", cellular_fixtures.to_csv().encode())},
    )
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_post_populate_with_error(mocker: MockFixture):
    mocker.patch("src.populate.pd.DataFrame.to_sql", return_value=None)

    response = client.post("/api/v1/populate", files={"file": ("test.csv", b"")})
    assert response.status_code == 400
    assert response.json() == {"detail": "Error parsing CSV file"}

    response = client.post(
        "/api/v1/populate",
        files={"file": ("test.csv", b"radio,mcc,net,area,cell,unit\n")},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "CSV file is empty"}
