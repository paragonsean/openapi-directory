from typing import List, Dict
from aiohttp import web

from openapi_server.models.booking_schema import BookingSchema
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hotel_booked_response import HotelBookedResponse
from openapi_server import util


async def create_booking(request: web.Request, request_body, ama_client_ref=None, accept_encoding=None) -> web.Response:
    """Create Orders associated to the Hotel Offers

    

    :param request_body: &#x60;offerId&#x60;, &#x60;guests&#x60;, &#x60;payments&#x60; and optional &#x60;rooms&#x60; for the repartition (when used the &#x60;rooms&#x60; array items must match the shopping offer &#x60;roomQuantity&#x60;) 
    :type request_body: dict | bytes
    :param ama_client_ref: Client Reference to track Request/Response
    :type ama_client_ref: str
    :param accept_encoding: Compress the Response
    :type accept_encoding: str

    """
    request_body = BookingSchema.from_dict(request_body)
    return web.Response(status=200)
