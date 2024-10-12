from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_collection_point_cart_collection_point_management_v1_select_collection_point_post_request import TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest
from openapi_server import util


async def temando_shipping_collection_point_guest_cart_collection_point_management_v1_select_collection_point_post(request: web.Request, cart_id, body=None) -> web.Response:
    """guest-carts/{cartId}/collection-point/select

    

    :param cart_id: 
    :type cart_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest.from_dict(body)
    return web.Response(status=200)
