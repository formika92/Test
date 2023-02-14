from typing import List, Dict

from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api.v1 import api_router as v1_api_router

api_routers: List[APIRouter] = [
    v1_api_router,
]

__all__ = ("api_routers",)
