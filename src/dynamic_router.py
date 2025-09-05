from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from random import randint

class Message(BaseModel):
    message: str

dynamic_router = APIRouter()
templates = Jinja2Templates(directory='src/templates')

@dynamic_router.get('/dynamic')
def route(request: Request, response_classe=HTMLResponse):
    return templates.TemplateResponse(
        'dynamic.html', {'request': request}
    )

@dynamic_router.get('/dynamic/data')
def route_roundint(request: Request, response_model=Message):
    return {'message': randint(1, 100)}

@dynamic_router.get('/polling')
def route_roundint(request: Request, response_model=Message):
    return templates.TemplateResponse(
        'polling.html', {'request': request}
    )