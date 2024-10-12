from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_order_query import FlightOrderQuery
from openapi_server.models.success_booking import SuccessBooking
from openapi_server import util


async def create_fligt_orders(request: web.Request, body) -> web.Response:
    """Create Order associated to the Flight offers.

    

    :param body: list of element needed to book a flight Order
    :type body: dict | bytes

    """
    body = FlightOrderQuery.from_dict(body)
    return web.Response(status=200)
