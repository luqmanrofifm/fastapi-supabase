from fastapi import APIRouter

router = APIRouter(tags=["Books"])

@router.get("")
async def get_books_list(
        
):
    return {"message": "get books list"}