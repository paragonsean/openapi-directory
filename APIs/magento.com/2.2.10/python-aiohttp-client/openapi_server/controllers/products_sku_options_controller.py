from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_custom_option_interface import CatalogDataProductCustomOptionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_custom_option_repository_v1_get_list_get(request: web.Request, sku) -> web.Response:
    """products/{sku}/options

    Get the list of custom options for a specific product

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)
