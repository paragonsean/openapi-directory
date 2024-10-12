from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_user_collection(request: web.Request, user_id, slug) -> web.Response:
    """Get user collection

    Returns a single collection associated with a user

    :param user_id: User id
    :type user_id: int
    :param slug: Collection slug
    :type slug: str

    """
    return web.Response(status=200)


async def get_user_collections(request: web.Request, user_id) -> web.Response:
    """Get user collections

    Returns a list of collections associated with a user

    :param user_id: User id
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_uploads_with_user(request: web.Request, username, limit=None, offset=None, page=None) -> web.Response:
    """Get user uploads with user

    Returns a list of uploads associated with a user

    :param username: Username
    :type username: str
    :param limit: Maximum number of results
    :type limit: int
    :param offset: Number of results to displace or skip over
    :type offset: int
    :param page: Number of results of limit length to displace or skip over
    :type page: int

    """
    return web.Response(status=200)
