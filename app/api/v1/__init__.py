from typing import Any, Dict
from fastapi import APIRouter

from . import test_func

api_prefix = "/v1"

api_router = APIRouter()
api_router.include_router(test_func.router, prefix=f"{api_prefix}", tags=["test"])

__all__ = ("api_router",)


@api_router.get(f"{api_prefix}/")
def get_status() -> Dict[str, Any]:
    return {"status": "ok"}
