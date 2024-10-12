from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_product_option_management_v1_save_post_request import BundleProductOptionManagementV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def bundle_product_option_management_v1_save_post(request: web.Request, body=None) -> web.Response:
    """bundle-products/options/add

    Add new option for bundle product

    :param body: 
    :type body: dict | bytes

    """
    body = BundleProductOptionManagementV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
