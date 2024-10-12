from typing import List, Dict
from aiohttp import web

from openapi_server.models.configurable_product_data_option_interface import ConfigurableProductDataOptionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def configurable_product_option_repository_v1_get_list_get(request: web.Request, sku) -> web.Response:
    """configurable-products/{sku}/options/all

    Get all options for configurable product

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)
