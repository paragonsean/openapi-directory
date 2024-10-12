from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_link_attribute_interface import CatalogDataProductLinkAttributeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_link_type_list_v1_get_item_attributes_get(request: web.Request, type) -> web.Response:
    """products/links/{type}/attributes

    Provide a list of the product link type attributes

    :param type: 
    :type type: str

    """
    return web.Response(status=200)
