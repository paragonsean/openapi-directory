from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_payment import NewPayment
from openapi_server.models.payment import Payment
from openapi_server.models.payment_list import PaymentList
from openapi_server import util


async def payment_get(request: web.Request, invoice_transaction_id=None, updated_after=None, page_size=None, page_number=None) -> web.Response:
    """Gets list of Payments

    

    :param invoice_transaction_id: Filter for Payments that have at least one allocation against a given Invoice Transaction ID
    :type invoice_transaction_id: int
    :param updated_after: Filter for Payments updated after a given date
    :type updated_after: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def payment_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Payment by Payment Transaction ID

    

    :param id: Invoice Transaction ID Number
    :type id: int

    """
    return web.Response(status=200)


async def payment_post(request: web.Request, model) -> web.Response:
    """Create new Payment and optionally assign payment allocations to Invoices

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewPayment.from_dict(model)
    return web.Response(status=200)
