from typing import List, Dict
from aiohttp import web

from openapi_server.models.capture_payment_out import CapturePaymentOut
from openapi_server.models.create_payment_in import CreatePaymentIn
from openapi_server.models.create_payment_out import CreatePaymentOut
from openapi_server.models.list_payments_out import ListPaymentsOut
from openapi_server import util


async def capture_payment(request: web.Request, key) -> web.Response:
    """Capture payment

    

    :param key: Transaction key.
    :type key: str

    """
    return web.Response(status=200)


async def create_payment(request: web.Request, key, input) -> web.Response:
    """Register a payment

    

    :param key: Transaction key.
    :type key: str
    :param input: Input
    :type input: dict | bytes

    """
    input = CreatePaymentIn.from_dict(input)
    return web.Response(status=200)


async def list_payments(request: web.Request, key, limit=None, offset=None) -> web.Response:
    """List payments

    

    :param key: Transaction key.
    :type key: str
    :param limit: Max record count (no more than 100, defaults to 10).
    :type limit: str
    :param offset: How many records need to be skipped, defaults to 0.
    :type offset: str

    """
    return web.Response(status=200)
