from fastapi import FastAPI
from routes.book import router as book_router
from routes.book_supabase import router as book_supabase_router

app = FastAPI()
app.include_router(book_router, prefix="/api/v1/psql/book", tags=["Books"])
app.include_router(book_supabase_router, prefix="/api/v1/supabase/book", tags=["Books Supabase"])




@app.get("/")
async def hello():
    return {"Hello": "CRUD FastAPI with supabase"}