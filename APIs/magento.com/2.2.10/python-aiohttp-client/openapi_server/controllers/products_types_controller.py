from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_type_interface import CatalogDataProductTypeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_type_list_v1_get_product_types_get(request: web.Request, ) -> web.Response:
    """products/types

    Retrieve available product types


    """
    return web.Response(status=200)
