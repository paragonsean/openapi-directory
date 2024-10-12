from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill_payment import BillPayment
from openapi_server.models.bill_payment_list import BillPaymentList
from openapi_server.models.new_bill_payment import NewBillPayment
from openapi_server import util


async def bill_payment_get(request: web.Request, updated_after=None, page_size=None, page_number=None) -> web.Response:
    """Gets list of Bill Payments

    

    :param updated_after: 
    :type updated_after: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def bill_payment_get_by_id(request: web.Request, id) -> web.Response:
    """Gets a Bill Payment by Payment Transaction ID

    

    :param id: Invoice Transaction ID Number
    :type id: int

    """
    return web.Response(status=200)


async def bill_payment_post(request: web.Request, model) -> web.Response:
    """Create new Bill Payment and optionally assign payment allocations to Bills

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewBillPayment.from_dict(model)
    return web.Response(status=200)
