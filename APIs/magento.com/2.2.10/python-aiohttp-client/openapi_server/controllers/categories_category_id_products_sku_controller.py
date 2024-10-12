from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_link_repository_v1_delete_by_ids_delete(request: web.Request, category_id, sku) -> web.Response:
    """categories/{categoryId}/products/{sku}

    Remove the product assignment from the category by category id and sku

    :param category_id: 
    :type category_id: str
    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)
