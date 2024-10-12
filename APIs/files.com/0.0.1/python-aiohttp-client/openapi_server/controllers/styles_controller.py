from typing import List, Dict
from aiohttp import web

from openapi_server.models.style_entity import StyleEntity
from openapi_server import util


async def delete_styles_path(request: web.Request, path) -> web.Response:
    """Delete Style

    Delete Style

    :param path: Style path.
    :type path: str

    """
    return web.Response(status=200)


async def get_styles_path(request: web.Request, path) -> web.Response:
    """Show Style

    Show Style

    :param path: Style path.
    :type path: str

    """
    return web.Response(status=200)


async def patch_styles_path(request: web.Request, path, file) -> web.Response:
    """Update Style

    Update Style

    :param path: Style path.
    :type path: str
    :param file: Logo for custom branding.
    :type file: str

    """
    return web.Response(status=200)
