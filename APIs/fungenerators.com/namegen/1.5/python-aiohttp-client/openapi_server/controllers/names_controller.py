from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def name_categories_get(request: web.Request, start=None, limit=None) -> web.Response:
    """name_categories_get

    Get available name generation categories.

    :param start: start
    :type start: int
    :param limit: limit
    :type limit: int

    """
    return web.Response(status=200)


async def name_generate_get(request: web.Request, category, suggest=None, start=None, limit=None, variation=None) -> web.Response:
    """name_generate_get

    Generated names in the given category

    :param category: Category to generator names from
    :type category: str
    :param suggest: Suggestion string if supported by this category generator.
    :type suggest: str
    :param start: start. Controls pagination. Relevant only if suggestion is supported
    :type start: int
    :param limit: limit. Controls pagination limit. Relevant only if suggestion is supported
    :type limit: int
    :param variation: Variation if supported ( male/female/any )
    :type variation: str

    """
    return web.Response(status=200)
