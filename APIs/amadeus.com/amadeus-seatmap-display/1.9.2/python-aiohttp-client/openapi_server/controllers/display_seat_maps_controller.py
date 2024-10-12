from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_offers import FlightOffers
from openapi_server.models.seat_map_reply import SeatMapReply
from openapi_server import util


async def get_seatmap_from_flight_offer(request: web.Request, x_http_method_override, body) -> web.Response:
    """Returns all the seat maps of a given flightOffer.

    

    :param x_http_method_override: the HTTP method to apply
    :type x_http_method_override: str
    :param body: 
    :type body: dict | bytes

    """
    body = FlightOffers.from_dict(body)
    return web.Response(status=200)


async def get_seatmap_from_order(request: web.Request, flight_order_id=None, flight_order_id2=None) -> web.Response:
    """Returns all the seat maps of a given order.

    

    :param flight_order_id: identifier of the order
    :type flight_order_id: str
    :param flight_order_id2: DEPRECATED identifier of the order , kept for backward compatibility
    :type flight_order_id2: str

    """
    return web.Response(status=200)
