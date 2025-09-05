from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .static import static_router
from .dynamic_router import dynamic_router
from .push import push_router

app = FastAPI()
app.mount(
    '/static',
    StaticFiles(directory='src/static'),
    name='static'
    )

app.include_router(static_router)
app.include_router(dynamic_router)
app.include_router(push_router)