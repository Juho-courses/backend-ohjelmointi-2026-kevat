from fastapi.testclient import TestClient

from app.main import app
from app.crud.author_crud import authors

client = TestClient(app)

INITIAL_AUTHORS = [
    {"id": 0, "name": "Author 1"},
    {"id": 1, "name": "Author 2"},
    {"id": 2, "name": "Author 3"},
]


def setup_function():
    authors.clear()
    authors.extend(INITIAL_AUTHORS)


def test_read_all_authors():
    response = client.get("/authors")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_read_all_authors_filter_by_name():
    response = client.get("/authors", params={"name": "Author 1"})
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["name"] == "Author 1"


def test_read_all_authors_filter_no_match():
    response = client.get("/authors", params={"name": "Unknown"})
    assert response.status_code == 200
    assert response.json() == []


def test_read_author_by_id():
    response = client.get("/authors/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Author 2"


def test_read_author_by_id_not_found():
    response = client.get("/authors/999")
    assert response.status_code == 404


def test_save_author():
    response = client.post("/authors", json={"name": "New Author"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "New Author"
    assert data["id"] == 3


def test_save_author_missing_field():
    response = client.post("/authors", json={})
    assert response.status_code == 422


def test_delete_author():
    response = client.delete("/authors/1")
    assert response.status_code == 204
    assert len(authors) == 2


def test_delete_author_not_found():
    response = client.delete("/authors/999")
    assert response.status_code == 404
