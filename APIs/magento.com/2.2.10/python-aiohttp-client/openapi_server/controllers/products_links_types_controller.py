from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_link_type_interface import CatalogDataProductLinkTypeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_link_type_list_v1_get_items_get(request: web.Request, ) -> web.Response:
    """products/links/types

    Retrieve information about available product link types


    """
    return web.Response(status=200)
