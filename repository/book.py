from sqlalchemy.orm import Session
from models.Book import Book
from sqlalchemy.sql.expression import select, func
from math import ceil
from typing import Optional

from schemas.book import CreateBookRequest

def get_all_books(
    db: Session,
    page: int = 1,
    page_size: int = 10,
    src:Optional[str] = '',
):
    limit = page_size
    offset = (page - 1) * limit

    query = (select(Book))
    query_count = (select(func.count(Book.id)))

    query = (
        query.limit(limit=limit)
        .offset(offset=offset)
    )

    data = db.execute(query).scalars().all()
    num_data = db.execute(query_count).scalar()
    num_page = ceil(num_data / limit)
    return (data, num_data, num_page)

def get_book_by_id(db: Session, id: str):
    query = (select(Book).filter(Book.id == id))
    return db.execute(query).scalar_one()

def create_book(db: Session, data: CreateBookRequest):
    book = Book(
        title=data.title,
        author=data.author,
        year=data.year,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book