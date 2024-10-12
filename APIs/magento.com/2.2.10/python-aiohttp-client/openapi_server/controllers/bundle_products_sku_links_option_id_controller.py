from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_product_link_management_v1_save_child_put_request import BundleProductLinkManagementV1SaveChildPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_link_management_v1_add_child_by_product_sku_post(request: web.Request, sku, option_id, body=None) -> web.Response:
    """bundle-products/{sku}/links/{optionId}

    Add child product to specified Bundle option by product sku

    :param sku: 
    :type sku: str
    :param option_id: 
    :type option_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = BundleProductLinkManagementV1SaveChildPutRequest.from_dict(body)
    return web.Response(status=200)
