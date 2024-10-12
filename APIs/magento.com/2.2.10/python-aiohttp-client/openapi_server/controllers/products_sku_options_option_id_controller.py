from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_custom_option_interface import CatalogDataProductCustomOptionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_custom_option_repository_v1_delete_by_identifier_delete(request: web.Request, sku, option_id) -> web.Response:
    """products/{sku}/options/{optionId}

    

    :param sku: 
    :type sku: str
    :param option_id: 
    :type option_id: int

    """
    return web.Response(status=200)


async def catalog_product_custom_option_repository_v1_get_get(request: web.Request, sku, option_id) -> web.Response:
    """products/{sku}/options/{optionId}

    Get custom option for a specific product

    :param sku: 
    :type sku: str
    :param option_id: 
    :type option_id: int

    """
    return web.Response(status=200)
