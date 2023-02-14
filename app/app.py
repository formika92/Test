from fastapi import FastAPI

import settings
from .api import api_routers

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

for router in api_routers:
    app.include_router(router)
