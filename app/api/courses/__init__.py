from fastapi import APIRouter

from .test import router as test_router


router = APIRouter(
    prefix='/courses',
    tags=['courses']
)
router.include_router(test_router)