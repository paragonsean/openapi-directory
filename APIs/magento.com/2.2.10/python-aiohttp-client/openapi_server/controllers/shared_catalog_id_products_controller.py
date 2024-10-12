from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def shared_catalog_product_management_v1_get_products_get(request: web.Request, id) -> web.Response:
    """sharedCatalog/{id}/products

    Return the list of product SKUs in the selected shared catalog.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
