from typing import List, Dict
from aiohttp import web

from openapi_server.models.calculate_price_response import CalculatePriceResponse
from openapi_server.models.error import Error
from openapi_server.models.purchase_request import PurchaseRequest
from openapi_server import util


async def reservation_order_calculate(request: web.Request, api_version, body) -> web.Response:
    """Calculate price for a &#x60;ReservationOrder&#x60;.

    Calculate price for placing a &#x60;ReservationOrder&#x60;.

    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str
    :param body: Information needed for calculate or purchase reservation
    :type body: dict | bytes

    """
    body = PurchaseRequest.from_dict(body)
    return web.Response(status=200)
