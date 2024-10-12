from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def configurable_product_link_management_v1_remove_child_delete(request: web.Request, sku, child_sku) -> web.Response:
    """configurable-products/{sku}/children/{childSku}

    Remove configurable product option

    :param sku: 
    :type sku: str
    :param child_sku: 
    :type child_sku: str

    """
    return web.Response(status=200)
