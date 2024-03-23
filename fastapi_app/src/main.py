from fastapi import FastAPI

from modules.apis.items_crud_api import router as crud_router
from modules.apis.frontend import router as frontend_router

from modules.utils.lifespan_event import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(crud_router, prefix="/api", tags=["crud_router"])
app.include_router(frontend_router, tags=["frontend_router"])