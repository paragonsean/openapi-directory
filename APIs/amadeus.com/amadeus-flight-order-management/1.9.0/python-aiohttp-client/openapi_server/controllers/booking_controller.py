from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success_booking import SuccessBooking
from openapi_server import util


async def cancel_flight_order(request: web.Request, flight_order_id) -> web.Response:
    """Cancel a given flight order

    

    :param flight_order_id: identifier of the flight order
    :type flight_order_id: str

    """
    return web.Response(status=200)


async def get_flight_order(request: web.Request, flight_order_id) -> web.Response:
    """Retrieve a given flight order

    

    :param flight_order_id: identifier of the flight order
    :type flight_order_id: str

    """
    return web.Response(status=200)
