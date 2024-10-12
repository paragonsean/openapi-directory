from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_category_interface import CatalogDataCategoryInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_repository_v1_delete_by_identifier_delete(request: web.Request, category_id) -> web.Response:
    """categories/{categoryId}

    Delete category by identifier

    :param category_id: 
    :type category_id: int

    """
    return web.Response(status=200)


async def catalog_category_repository_v1_get_get(request: web.Request, category_id, store_id=None) -> web.Response:
    """categories/{categoryId}

    Get info about category by category id

    :param category_id: 
    :type category_id: int
    :param store_id: 
    :type store_id: int

    """
    return web.Response(status=200)
