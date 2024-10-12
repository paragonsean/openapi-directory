from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_categories(request: web.Request, lang) -> web.Response:
    """Get categories

    Get the list of all the categories in TV &amp; iPlayer.

    :param lang: The language for any applicable localised strings.
    :type lang: str

    """
    return web.Response(status=200)


async def get_sub_categories(request: web.Request, category, lang) -> web.Response:
    """Get sub-categories

    Get sub-categories

    :param category: The category identifier to return results from.
    :type category: str
    :param lang: The language for any applicable localised strings.
    :type lang: str

    """
    return web.Response(status=200)
