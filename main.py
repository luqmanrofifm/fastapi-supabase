from fastapi import FastAPI
# from .routes import router

app = FastAPI()
# app.include_router(router)


@app.get("/")
async def hello():
    return {"Hello": "CRUD FastAPI with supabase"}