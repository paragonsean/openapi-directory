from typing import List, Dict
from aiohttp import web

from openapi_server.models.configurable_product_link_management_v1_add_child_post_request import ConfigurableProductLinkManagementV1AddChildPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def configurable_product_link_management_v1_add_child_post(request: web.Request, sku, body=None) -> web.Response:
    """configurable-products/{sku}/child

    

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConfigurableProductLinkManagementV1AddChildPostRequest.from_dict(body)
    return web.Response(status=200)
