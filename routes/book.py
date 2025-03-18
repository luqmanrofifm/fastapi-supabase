from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from db.postgres import get_db_sync
from repository import book as book_repo
from core.responses import Created, common_response, BadRequest, Ok
from schemas.book import CreateBookRequest

router = APIRouter(tags=["Books"])

@router.get("/list")
async def get_books_list(
    db: Session = Depends(get_db_sync),
    page: int = 1,
    page_size: int = 10,
):
    try:
        data, num_data, num_page = book_repo.get_all_books(db)
        return common_response(
            Ok(
                data={
                    "count": num_data,
                    "page_count": num_page,
                    "page_size": page_size,
                    "page": page,
                    "data": [
                        {
                            "id": str(book.id),
                            "title": book.title,
                            "author": book.author,
                            "year": book.year,
                        }
                        for book in data
                    ]
                }
            )
        )
    except Exception as e:
        return common_response(BadRequest(message='Failed to get book data', error=str(e)))
    
@router.get("/detail/{id}")
async def get_book_detail(
    db: Session = Depends(get_db_sync),
    id: str = None,
):
    try:
        data = book_repo.get_book_by_id(db, id)
        return common_response(
            Ok(
                data={
                    "id": str(data.id),
                    "title": data.title,
                    "author": data.author,
                    "year": data.year,
                }
            )
        )
    except Exception as e:
        return common_response(BadRequest(message='Failed to get book data', error=str(e)))
    

@router.post("/create")
async def create_book(
    db: Session = Depends(get_db_sync),
    payload: CreateBookRequest = None,
):  
    try:
        data = book_repo.create_book(db, payload)
        return common_response(Created(
            data={
                "id": str(data.id),
                "title": data.title,
                "author": data.author,
                "year": data.year,
            }
        ))
    except Exception as e:
        return common_response(BadRequest(message='Failed to create book data', error=str(e)))