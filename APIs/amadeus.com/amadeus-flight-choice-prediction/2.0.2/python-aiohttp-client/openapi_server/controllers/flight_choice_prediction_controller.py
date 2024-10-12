from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_offers_search_reply import FlightOffersSearchReply
from openapi_server.models.success import Success
from openapi_server import util


async def get_flight_choice_predict(request: web.Request, x_http_method_override, body) -> web.Response:
    """Predict the choice of flight offers.

    

    :param x_http_method_override: the HTTP method to apply
    :type x_http_method_override: str
    :param body: 
    :type body: dict | bytes

    """
    body = FlightOffersSearchReply.from_dict(body)
    return web.Response(status=200)
