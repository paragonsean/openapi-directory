from typing import List, Dict
from aiohttp import web

from openapi_server.models.language_wrapped import LanguageWrapped
from openapi_server import util


async def resources_languages_id_json_get(request: web.Request, id) -> web.Response:
    """Get Language by ID

    Information about a specific language

    :param id: The id of the language to look up
    :type id: int

    """
    return web.Response(status=200)


async def resources_languages_json_get(request: web.Request, max=None, offset=None, sort=None) -> web.Response:
    """Get Languages

    Language Listings

    :param max: The maximum number of records to return
    :type max: int
    :param offset: Return records starting at the offset index.
    :type offset: int
    :param sort: The name of the property to which sorting will be applied
    :type sort: str

    """
    return web.Response(status=200)
