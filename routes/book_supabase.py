
from fastapi import APIRouter
from fastapi.params import Depends
from supabase import Client

from db.supabase import get_supabase
from repository import book_supabase as book_repo
from routes import book
from schemas.book import CreateBookRequest


router = APIRouter(tags=["Books Supabase"])

@router.get("/list")
async def get_books_list(
    db_supabase: Client = Depends(get_supabase),
    page: int = 1,
    page_size: int = 10,
):
    """
    Get all books from supabase
    """
    data, num_data, num_page = await book_repo.get_all_books(db_supabase, page, page_size)
    return {
        "count": num_data,
        "page_count": num_page,
        "page_size": page_size,
        "page": page,
        "data": [
            {
                "id": str(book["id"]),
                "title": book["title"],
                "author": book["author"],
                "year": book["year"],
            }
            for book in data.data
        ],
    }

@router.post("/create")
async def create_book(
    db_supabase: Client = Depends(get_supabase),
    payload: CreateBookRequest = None,
):  
    """
    Create a book in supabase
    """
    try:
        data = await book_repo.create_book(db_supabase, payload)
        return {
            "id": str(data["id"]),
            "title": data["title"],
            "author": data["author"],
            "year": data["year"],
        }
    except Exception as e:
        print(e)
        return {
            "message": "Failed to create book",
            "error": str(e),
        }