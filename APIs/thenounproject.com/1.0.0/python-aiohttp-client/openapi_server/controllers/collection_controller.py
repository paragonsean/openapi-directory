from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_collection_by_id(request: web.Request, id) -> web.Response:
    """Get collection by id

    Returns a single collection

    :param id: Collection id
    :type id: int

    """
    return web.Response(status=200)


async def get_collection_by_slug(request: web.Request, slug) -> web.Response:
    """Get collection by slug

    Returns a single collection

    :param slug: Collection slug
    :type slug: str

    """
    return web.Response(status=200)


async def get_collection_icons_by_id(request: web.Request, id, limit=None, offset=None, page=None) -> web.Response:
    """Get collection icons by id

    Returns a list of icons associated with a collection

    :param id: Collection id
    :type id: int
    :param limit: Maximum number of results
    :type limit: int
    :param offset: Number of results to displace or skip over
    :type offset: int
    :param page: Number of results of limit length to displace or skip over
    :type page: int

    """
    return web.Response(status=200)


async def get_collection_icons_by_slug(request: web.Request, slug, limit=None, offset=None, page=None) -> web.Response:
    """Get collection icons by slug

    Returns a list of icons associated with a collection

    :param slug: Collection slug
    :type slug: str
    :param limit: Maximum number of results
    :type limit: int
    :param offset: Number of results to displace or skip over
    :type offset: int
    :param page: Number of results of limit length to displace or skip over
    :type page: int

    """
    return web.Response(status=200)
