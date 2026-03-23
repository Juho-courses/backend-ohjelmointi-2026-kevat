from fastapi.testclient import TestClient

from app.main import app
from app.db.models import AuthorDb

client = TestClient(app)


def seed_authors(session):
    session.add(AuthorDb(name="Author 1"))
    session.add(AuthorDb(name="Author 2"))
    session.add(AuthorDb(name="Author 3"))
    session.commit()


def test_read_all_authors(session):
    seed_authors(session)
    response = client.get("/authors")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_read_all_authors_filter_by_name(session):
    seed_authors(session)
    response = client.get("/authors", params={"name": "Author 1"})
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["name"] == "Author 1"


def test_read_all_authors_filter_no_match(session):
    seed_authors(session)
    response = client.get("/authors", params={"name": "Unknown"})
    assert response.status_code == 200
    assert response.json() == []


def test_read_author_by_id(session):
    seed_authors(session)
    response = client.get("/authors/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Author 1"


def test_read_author_by_id_not_found():
    response = client.get("/authors/999")
    assert response.status_code == 404


def test_save_author():
    response = client.post("/authors", json={"name": "New Author"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "New Author"
    assert "id" in data


def test_save_author_missing_field():
    response = client.post("/authors", json={})
    assert response.status_code == 422


def test_delete_author(session):
    seed_authors(session)
    response = client.delete("/authors/1")
    assert response.status_code == 204
    response = client.get("/authors")
    assert len(response.json()) == 2


def test_delete_author_not_found():
    response = client.delete("/authors/999")
    assert response.status_code == 404
