from fastapi import FastAPI

health_app = FastAPI(title="Simple Health System")

@health_app.get("/")
async def root():
    return {"message": "Welcome to the Health System API"}