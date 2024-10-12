from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def riddle_random_get(request: web.Request, category=None) -> web.Response:
    """riddle_random_get

    Get a random riddle for a given category(optional)

    :param category: Category to get the riddle from
    :type category: str

    """
    return web.Response(status=200)


async def riddle_search_get(request: web.Request, query=None, category=None) -> web.Response:
    """riddle_search_get

    Search for random riddle which has the text in the query, for a given category(optional).

    :param query: Text to search for in the riddle
    :type query: str
    :param category: Category to get the riddle from
    :type category: str

    """
    return web.Response(status=200)
