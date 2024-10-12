from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_base_price_storage_v1_get_post_request import CatalogBasePriceStorageV1GetPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_cost_storage_v1_delete_post(request: web.Request, body=None) -> web.Response:
    """products/cost-delete

    Delete product cost. In case of at least one of skus is not found exception will be thrown. If error occurred during the delete exception will be thrown.

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogBasePriceStorageV1GetPostRequest.from_dict(body)
    return web.Response(status=200)
