from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_type_interface import CatalogDataProductAttributeTypeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_types_list_v1_get_items_get(request: web.Request, ) -> web.Response:
    """products/attributes/types

    Retrieve list of product attribute types


    """
    return web.Response(status=200)
