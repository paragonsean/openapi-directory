from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_product_link_management_v1_save_child_put_request import BundleProductLinkManagementV1SaveChildPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_link_management_v1_save_child_put(request: web.Request, sku, id, body=None) -> web.Response:
    """bundle-products/{sku}/links/{id}

    

    :param sku: 
    :type sku: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BundleProductLinkManagementV1SaveChildPutRequest.from_dict(body)
    return web.Response(status=200)
