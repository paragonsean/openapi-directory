from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_link_repository_v1_delete_by_id_delete(request: web.Request, sku, type, linked_product_sku) -> web.Response:
    """products/{sku}/links/{type}/{linkedProductSku}

    

    :param sku: 
    :type sku: str
    :param type: 
    :type type: str
    :param linked_product_sku: 
    :type linked_product_sku: str

    """
    return web.Response(status=200)
