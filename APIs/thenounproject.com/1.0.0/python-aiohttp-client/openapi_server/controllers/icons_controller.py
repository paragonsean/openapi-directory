from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_icons_by_term(request: web.Request, term, limit_to_public_domain=None, limit=None, offset=None, page=None) -> web.Response:
    """Get icons by term

    Returns a list of icons

    :param term: Icon term
    :type term: str
    :param limit_to_public_domain: Limit results to public domain icons only
    :type limit_to_public_domain: int
    :param limit: Maximum number of results
    :type limit: int
    :param offset: Number of results to displace or skip over
    :type offset: int
    :param page: Number of results of limit length to displace or skip over
    :type page: int

    """
    return web.Response(status=200)


async def get_recent_icons(request: web.Request, limit=None, offset=None, page=None) -> web.Response:
    """Get recent icons

    Returns list of most recently uploaded icons

    :param limit: Maximum number of results
    :type limit: int
    :param offset: Number of results to displace or skip over
    :type offset: int
    :param page: Number of results of limit length to displace or skip over
    :type page: int

    """
    return web.Response(status=200)
