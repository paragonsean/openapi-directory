from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_custom_option_type_interface import CatalogDataProductCustomOptionTypeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_custom_option_type_list_v1_get_items_get(request: web.Request, ) -> web.Response:
    """products/options/types

    Get custom option types


    """
    return web.Response(status=200)
