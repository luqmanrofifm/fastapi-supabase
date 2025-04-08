from math import ceil
from supabase import Client

from schemas.book import CreateBookRequest


async def get_all_books(
    db: Client,
    page: int = 1,
    page_size: int = 10,
):
    """
    Get all books from supabase
    """
    limit = page_size
    offset = (page - 1) * limit

    data = db.table("book").select("*").range(offset, offset + limit - 1).execute()
    num_data = db.table("book").select("*", count="exact").execute().count
    if num_data is None:
        num_data = 0
    num_page = ceil(num_data / limit)

    print(num_data)
    return data, num_data, num_page

async def create_book(
    db: Client,
    data: CreateBookRequest,
):
    """
    Create a book in supabase
    """
    book = {
        "title": data.title,
        "author": data.author,
        "year": data.year,
    }
    response = db.table("book").insert(book).execute()
    return response.data[0] if response.data else None