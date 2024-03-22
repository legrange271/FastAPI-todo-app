from fastapi import APIRouter

router = APIRouter()

@router.get("/", status_code=200)
def home():
    """Return simple hello world"""
    return {"message": "Hello world!"}