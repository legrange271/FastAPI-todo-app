from fastapi import FastAPI, Response, status
from modules.models.models import Item, items

from modules.apis.items_crud_api import router as crud_router
from modules.apis.frontend import router as frontend_router

app = FastAPI()

app.include_router(crud_router, prefix="/api", tags=["crud_router"])
app.include_router(frontend_router, tags=["frontend_router"])
