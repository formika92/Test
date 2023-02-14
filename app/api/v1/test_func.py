from time import monotonic

from fastapi import APIRouter

from app.api.v1.schemas import TestResponse
from app.utils import work

router = APIRouter()


@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    await work()
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
