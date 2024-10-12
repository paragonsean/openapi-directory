from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.patch import Patch
from openapi_server.models.reservation_response import ReservationResponse
from openapi_server import util


async def reservation_update_0(request: web.Request, reservation_order_id, reservation_id, api_version, parameters) -> web.Response:
    """Updates a &#x60;Reservation&#x60;.

    Updates the applied scopes of the &#x60;Reservation&#x60;.

    :param reservation_order_id: Order Id of the reservation 
    :type reservation_order_id: str
    :param reservation_id: Id of the Reservation Item
    :type reservation_id: str
    :param api_version: Supported version.
    :type api_version: str
    :param parameters: Information needed to patch a reservation item
    :type parameters: dict | bytes

    """
    parameters = Patch.from_dict(parameters)
    return web.Response(status=200)
