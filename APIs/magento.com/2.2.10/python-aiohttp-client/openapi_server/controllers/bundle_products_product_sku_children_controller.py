from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_data_link_interface import BundleDataLinkInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_link_management_v1_get_children_get(request: web.Request, product_sku, option_id=None) -> web.Response:
    """bundle-products/{productSku}/children

    Get all children for Bundle product

    :param product_sku: 
    :type product_sku: str
    :param option_id: 
    :type option_id: int

    """
    return web.Response(status=200)
