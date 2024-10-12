from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_link_interface import CatalogDataProductLinkInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_link_management_v1_get_linked_items_by_type_get(request: web.Request, sku, type) -> web.Response:
    """products/{sku}/links/{type}

    Provide the list of links for a specific product

    :param sku: 
    :type sku: str
    :param type: 
    :type type: str

    """
    return web.Response(status=200)
