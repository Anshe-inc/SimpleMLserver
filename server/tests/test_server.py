import pytest
from aiohttp import web
import aiohttp_jinja2
import jinja2

from server.router import router
from server.views import model


@pytest.fixture
def cli(loop, aiohttp_client, aiohttp_unused_port):
    port = aiohttp_unused_port()

    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    router.assign_routes(app.router)

    app['model'] = model.load()
    return loop.run_until_complete(aiohttp_client(app, server_kwargs={'port': port}))


@pytest.mark.asyncio
async def test_predict_invalid_method(cli):
    resp = await cli.get('/predict')
    assert resp.status == 405
