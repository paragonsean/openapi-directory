from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.reservation_response import ReservationResponse
from openapi_server.models.split_request import SplitRequest
from openapi_server import util


async def reservation_split(request: web.Request, reservation_order_id, api_version, body) -> web.Response:
    """Split the &#x60;Reservation&#x60;.

    Split a &#x60;Reservation&#x60; into two &#x60;Reservation&#x60;s with specified quantity distribution. 

    :param reservation_order_id: Order Id of the reservation 
    :type reservation_order_id: str
    :param api_version: Supported version.
    :type api_version: str
    :param body: Information needed to Split a reservation item
    :type body: dict | bytes

    """
    body = SplitRequest.from_dict(body)
    return web.Response(status=200)
