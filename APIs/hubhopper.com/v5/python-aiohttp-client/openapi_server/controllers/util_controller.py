from typing import List, Dict
from aiohttp import web

from openapi_server.models.language_list import LanguageList
from openapi_server import util


async def util_languages_get(request: web.Request, page_size=None, page=None) -> web.Response:
    """util_languages_get

    

    :param page_size: Provide the size of the page to fetch.
    :type page_size: str
    :param page: Provide the page number to fetch.
    :type page: str

    """
    return web.Response(status=200)
