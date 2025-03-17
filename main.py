from fastapi import FastAPI
from routes.book import router as book_router

app = FastAPI()
app.include_router(book_router, prefix="/books", tags=["Books"])




@app.get("/")
async def hello():
    return {"Hello": "CRUD FastAPI with supabase"}