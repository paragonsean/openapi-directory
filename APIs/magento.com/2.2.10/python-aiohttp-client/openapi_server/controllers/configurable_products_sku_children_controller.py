from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_interface import CatalogDataProductInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def configurable_product_link_management_v1_get_children_get(request: web.Request, sku) -> web.Response:
    """configurable-products/{sku}/children

    Get all children for Configurable product

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)
