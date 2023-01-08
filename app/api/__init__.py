from fastapi import APIRouter

from .auth import router as auth_router
from .roles import router as roles_router
from .courses import router as courses_router


router = APIRouter(
    prefix='/api',
)
router.include_router(auth_router)
router.include_router(roles_router)
router.include_router(courses_router)