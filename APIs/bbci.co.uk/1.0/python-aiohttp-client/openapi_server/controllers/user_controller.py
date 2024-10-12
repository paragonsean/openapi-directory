from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_user_store_purchases(request: web.Request, identity_cookie) -> web.Response:
    """Get user store purchases

    Get user store purchases

    :param identity_cookie: The BBC-id cookie value
    :type identity_cookie: float

    """
    return web.Response(status=200)


async def get_user_store_recommendations(request: web.Request, identity_cookie) -> web.Response:
    """Get user store recommendations

    Get user store recommendations

    :param identity_cookie: The BBC-id cookie value
    :type identity_cookie: float

    """
    return web.Response(status=200)


async def get_user_watching(request: web.Request, identity_cookie) -> web.Response:
    """Get user watching

    Get user watching

    :param identity_cookie: The BBC-id cookie value
    :type identity_cookie: float

    """
    return web.Response(status=200)
