from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.properties import Properties
from openapi_server import util


async def reservation_available_scopes(request: web.Request, reservation_order_id, reservation_id, api_version, body) -> web.Response:
    """Get Available Scopes for &#x60;Reservation&#x60;.

    Get Available Scopes for &#x60;Reservation&#x60;. 

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param reservation_id: Id of the Reservation Item
    :type reservation_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str
    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)
