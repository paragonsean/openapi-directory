from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def taunt_categories_get(request: web.Request, start=None, limit=None) -> web.Response:
    """taunt_categories_get

    Get available taunt generation categories.

    :param start: start
    :type start: int
    :param limit: limit
    :type limit: int

    """
    return web.Response(status=200)


async def taunt_generate_get(request: web.Request, category, limit=None) -> web.Response:
    """taunt_generate_get

    Generated taunts in the given category

    :param category: Category to generator taunt from
    :type category: str
    :param limit: Limit. Controls number of taunts generated. Max of 5-10 based on the plan
    :type limit: int

    """
    return web.Response(status=200)
