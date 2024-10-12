from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_data_option_type_interface import BundleDataOptionTypeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_option_type_list_v1_get_items_get(request: web.Request, ) -> web.Response:
    """bundle-products/options/types

    Get all types for options for bundle products


    """
    return web.Response(status=200)
