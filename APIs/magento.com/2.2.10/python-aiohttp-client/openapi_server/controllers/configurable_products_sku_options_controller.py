from typing import List, Dict
from aiohttp import web

from openapi_server.models.configurable_product_option_repository_v1_save_post_request import ConfigurableProductOptionRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def configurable_product_option_repository_v1_save_post(request: web.Request, sku, body=None) -> web.Response:
    """configurable-products/{sku}/options

    Save option

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConfigurableProductOptionRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
