import logging
import sys

from aiohttp import web
import aiohttp_jinja2
import jinja2

from server import config
from server.router import router
from server.views import model


def set_logger_settings():
    logging.basicConfig(level='INFO', stream=sys.stdout)


def main():
    app = web.Application()
    app['model'] = model.load()
    app['config'] = config

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(config.CONFIG['templates_path']))
    router.assign_routes(app.router)
    set_logger_settings()

    web.run_app(app, port=config.CONFIG['port'])


if __name__ == '__main__':
    main()
