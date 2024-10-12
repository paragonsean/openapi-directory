from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.merge_request import MergeRequest
from openapi_server.models.reservation_response import ReservationResponse
from openapi_server import util


async def reservation_merge(request: web.Request, reservation_order_id, api_version, body) -> web.Response:
    """Merges two &#x60;Reservation&#x60;s.

    Merge the specified &#x60;Reservation&#x60;s into a new &#x60;Reservation&#x60;. The two &#x60;Reservation&#x60;s being merged must have same properties.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str
    :param body: Information needed for commercial request for a reservation
    :type body: dict | bytes

    """
    body = MergeRequest.from_dict(body)
    return web.Response(status=200)
