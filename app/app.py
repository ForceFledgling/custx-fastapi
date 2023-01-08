from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.middleware.cors import CORSMiddleware

from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Registration , authentication and authorization',
    },
    {
        'name': 'roles',
        'description': 'User role management',
    },
    {
        'name': 'instructors',
        'description': 'Instructor working hours',
    },
    {
        'name': 'rooms',
        'description': 'Working with dressing rooms',
    },
    {
        'name': 'groups',
        'description': 'Working with swimming groups',
    },
]


app = FastAPI(
    title='CustX',
    description='API service for the CustX project',
    version='0.0.1',
    openapi_tags=tags_metadata,
)
app.include_router(router)

origins = [
    "http://localhost:3000",
    "https://www.custx.ru",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = TestClient(app)
