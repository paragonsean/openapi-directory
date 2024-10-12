from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_collection_point_cart_collection_point_management_v1_select_collection_point_post_request import TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest
from openapi_server import util


async def temando_shipping_collection_point_cart_collection_point_management_v1_select_collection_point_post(request: web.Request, body=None) -> web.Response:
    """carts/mine/collection-point/select

    

    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest.from_dict(body)
    return web.Response(status=200)
