from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_request_response import AddRequestResponse
from openapi_server.models.create_payment_request import CreatePaymentRequest
from openapi_server.models.payment_request_state_response import PaymentRequestStateResponse
from openapi_server import util


async def add_payment_request(request: web.Request, body) -> web.Response:
    """Creates a new payment request. Will return request id to check for transaction state and ergopay url to show the user as QR code

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePaymentRequest.from_dict(body)
    return web.Response(status=200)


async def get_payment_state(request: web.Request, request_id) -> web.Response:
    """Returns the state of a payment request. Please note that payment requests are purged after some time, so persist the state at your side when needed

    

    :param request_id: 
    :type request_id: str

    """
    return web.Response(status=200)
