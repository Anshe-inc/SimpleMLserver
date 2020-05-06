from aiohttp import web

from server.handlers import predict
from server.handlers import root
from server import config


def assign_routes(router: web.UrlDispatcher) -> None:
    router.add_routes([
        web.post('/predict', predict.handle),
        web.get('/', root.handle),
        web.static('/templates', config.CONFIG['templates_path']),
    ])
