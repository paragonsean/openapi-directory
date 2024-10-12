from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.purchase_request import PurchaseRequest
from openapi_server.models.reservation_order_response import ReservationOrderResponse
from openapi_server import util


async def reservation_order_purchase(request: web.Request, reservation_order_id, api_version, body) -> web.Response:
    """Purchase &#x60;ReservationOrder&#x60;

    Purchase &#x60;ReservationOrder&#x60; and create resource under the specified URI.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str
    :param body: Information needed for calculate or purchase reservation
    :type body: dict | bytes

    """
    body = PurchaseRequest.from_dict(body)
    return web.Response(status=200)
