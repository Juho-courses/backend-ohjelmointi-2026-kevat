from fastapi.testclient import TestClient

from app.main import app
from app.db.models import BookOut

client = TestClient(app)


def seed_books(session):
    session.add(BookOut(title="Book 1", author="Author 1"))
    session.add(BookOut(title="Book 2", author="Author 2"))
    session.add(BookOut(title="Book 3", author="Author 1"))
    session.commit()


def test_read_all_books(session):
    seed_books(session)
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_read_all_books_filter_by_author(session):
    seed_books(session)
    response = client.get("/books", params={"author": "Author 1"})
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 2
    assert all(b["author"] == "Author 1" for b in data)


def test_read_all_books_filter_no_match(session):
    seed_books(session)
    response = client.get("/books", params={"author": "Unknown"})
    assert response.status_code == 200
    assert response.json() == []


def test_read_book_by_id(session):
    seed_books(session)
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Book 1"


def test_read_book_by_id_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404


def test_save_book():
    response = client.post(
        "/books", json={"title": "New Book", "author": "New Author"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "New Book"
    assert data["author"] == "New Author"
    assert "id" in data


def test_save_book_missing_field():
    response = client.post("/books", json={"title": "No Author"})
    assert response.status_code == 422


def test_delete_book(session):
    seed_books(session)
    response = client.delete("/books/1")
    assert response.status_code == 204
    response = client.get("/books")
    assert len(response.json()) == 2


def test_delete_book_not_found():
    response = client.delete("/books/999")
    assert response.status_code == 404
