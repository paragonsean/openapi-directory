from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_data_collection_point_quote_collection_point_interface import TemandoShippingDataCollectionPointQuoteCollectionPointInterface
from openapi_server import util


async def temando_shipping_collection_point_guest_cart_collection_point_management_v1_get_collection_points_get(request: web.Request, cart_id) -> web.Response:
    """guest-carts/{cartId}/collection-point/search-result

    

    :param cart_id: 
    :type cart_id: str

    """
    return web.Response(status=200)
