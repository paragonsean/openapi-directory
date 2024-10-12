from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_checkout_request import CreateCheckoutRequest
from openapi_server.models.create_checkout_response import CreateCheckoutResponse
from openapi_server import util


async def create_checkout(request: web.Request, location_id, body) -> web.Response:
    """CreateCheckout

    Links a &#x60;checkoutId&#x60; to a &#x60;checkout_page_url&#x60; that customers are directed to in order to provide their payment information using a payment processing workflow hosted on connect.squareup.com.

    :param location_id: The ID of the business location to associate the checkout with.
    :type location_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateCheckoutRequest.from_dict(body)
    return web.Response(status=200)
