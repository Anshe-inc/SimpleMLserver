import aiohttp_jinja2
import typing as tp
from aiohttp import web


@aiohttp_jinja2.template('index.html')
async def handle(request: web.Request) -> tp.Dict[str, str]:
    return {'result': ''}
