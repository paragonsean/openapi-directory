from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_link_management_v1_remove_child_delete(request: web.Request, sku, option_id, child_sku) -> web.Response:
    """bundle-products/{sku}/options/{optionId}/children/{childSku}

    Remove product from Bundle product option

    :param sku: 
    :type sku: str
    :param option_id: 
    :type option_id: int
    :param child_sku: 
    :type child_sku: str

    """
    return web.Response(status=200)
