import re
from io import BytesIO

from fastapi import FastAPI
from fastapi.requests import Request
from requests_html import HTMLSession
from starlette.responses import StreamingResponse

app = FastAPI()


@app.get('/')
async def get_image(request: Request):
    path = re.findall(r'path=(.*)', request.url.query)[0]

    with HTMLSession() as session:
        res = session.get(path)

    return StreamingResponse(
        BytesIO(res.content), media_type=res.headers.get('Content-Type')
    )
