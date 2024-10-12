from typing import List, Dict
from aiohttp import web

from openapi_server.models.big_oven_model_api2_collection_info import BigOvenModelAPI2CollectionInfo
from openapi_server.models.big_oven_model_api2_recipe_search_result import BigOvenModelAPI2RecipeSearchResult
from openapi_server import util


async def collection_collections(request: web.Request, test=None) -> web.Response:
    """Get the list of current, seasonal recipe collections. From here, you can use the /collection/{id} endpoint to retrieve the recipes in those collections.

    

    :param test: 
    :type test: str

    """
    return web.Response(status=200)


async def collection_get_collection(request: web.Request, id, rpp=None, pg=None, test=None, session_for_logging=None) -> web.Response:
    """Gets a recipe collection. A recipe collection is a curated set of recipes.

    

    :param id: the collection identifier
    :type id: int
    :param rpp: results per page
    :type rpp: int
    :param pg: page number (starting with 1)
    :type pg: int
    :param test: 
    :type test: bool
    :param session_for_logging: 
    :type session_for_logging: str

    """
    return web.Response(status=200)


async def collection_get_collection_meta(request: web.Request, id) -> web.Response:
    """Gets a recipe collection metadata. A recipe collection is a curated set of recipes.

    

    :param id: the collection identifier
    :type id: int

    """
    return web.Response(status=200)
