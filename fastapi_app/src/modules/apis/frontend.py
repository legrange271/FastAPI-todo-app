from fastapi import APIRouter

router = APIRouter()

@router.get("/", status_code=200)
def home():
    """Specify basic app functionality"""
    return {"message": "Hello world!"}