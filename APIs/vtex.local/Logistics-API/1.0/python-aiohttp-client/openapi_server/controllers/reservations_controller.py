from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_reservation200_response import CreateReservation200Response
from openapi_server.models.create_reservation_request1 import CreateReservationRequest1
from openapi_server.models.reservation_by_id200_response import ReservationById200Response
from openapi_server import util


async def acknowledgment_reservation(request: web.Request, content_type, accept, reservation_id) -> web.Response:
    """Acknowledgment reservation

    Acknowledges reservations made by reservation ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param reservation_id: 
    :type reservation_id: str

    """
    return web.Response(status=200)


async def cancel_reservation(request: web.Request, content_type, accept, reservation_id) -> web.Response:
    """Cancel reservation

    Cancels reservation by reservation ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param reservation_id: 
    :type reservation_id: str

    """
    return web.Response(status=200)


async def confirm_reservation(request: web.Request, content_type, accept, reservation_id) -> web.Response:
    """Confirm reservation

    Confirms reservation by reservation ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param reservation_id: 
    :type reservation_id: str

    """
    return web.Response(status=200)


async def create_reservation(request: web.Request, accept, content_type, body) -> web.Response:
    """Create reservation

    Creates [reservation](https://help.vtex.com/en/tutorial/how-does-reservation-work--tutorials_92).

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateReservationRequest1.from_dict(body)
    return web.Response(status=200)


async def reservation_by_id(request: web.Request, content_type, accept, reservation_id) -> web.Response:
    """List reservation by ID

    Lists reservation&#39;s information by ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param reservation_id: 
    :type reservation_id: str

    """
    return web.Response(status=200)


async def reservationby_warehouseand_sku(request: web.Request, content_type, accept, warehouse_id, sku_id) -> web.Response:
    """List reservation by warehouse and SKU

    Lists reservations in your store, by searching through warehouse and SKU.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param warehouse_id: 
    :type warehouse_id: str
    :param sku_id: 
    :type sku_id: str

    """
    return web.Response(status=200)
