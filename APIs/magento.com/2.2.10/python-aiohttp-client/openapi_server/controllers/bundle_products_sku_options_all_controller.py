from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_data_option_interface import BundleDataOptionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_option_repository_v1_get_list_get(request: web.Request, sku) -> web.Response:
    """bundle-products/{sku}/options/all

    Get all options for bundle product

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)
