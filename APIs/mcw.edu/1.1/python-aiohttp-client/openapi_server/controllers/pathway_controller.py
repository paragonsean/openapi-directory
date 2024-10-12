from typing import List, Dict
from aiohttp import web

from openapi_server.models.pathway import Pathway
from openapi_server import util


async def get_pathways_with_diagrams_for_category_using_get(request: web.Request, category) -> web.Response:
    """Return a list of pathways based on category provided

    

    :param category: Pathway Category
    :type category: str

    """
    return web.Response(status=200)


async def search_pathways_using_get(request: web.Request, search_string) -> web.Response:
    """Return a list of pathways based on search term

    

    :param search_string: Free text search string
    :type search_string: str

    """
    return web.Response(status=200)
