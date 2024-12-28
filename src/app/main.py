from fastapi import FastAPI

from src.app.routes.greeter import router_router
from src.app.configuration import settings

app = FastAPI()
app.include_router(router=router_router, prefix=f"/{settings.APPLICATION}/{settings.API_VERSION}")

