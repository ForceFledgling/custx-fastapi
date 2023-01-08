import uvicorn

from .settings import settings


uvicorn.run(
    'app.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
    ssl_keyfile='/etc/letsencrypt/live/api.custx.ru/privkey.pem',
    ssl_certfile='/etc/letsencrypt/live/api.custx.ru/fullchain.pem'
)
