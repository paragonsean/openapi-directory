from typing import List, Dict
from aiohttp import web

from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_list import InvoiceList
from openapi_server.models.new_invoice import NewInvoice
from openapi_server import util


async def invoice_get(request: web.Request, updated_after=None, page_size=None, page_number=None, sort=None, company_idfk=None) -> web.Response:
    """Gets list of Invoices

    TransactionStatusCode values are: \&quot;Draft\&quot;, \&quot;Sent\&quot;, \&quot;Late\&quot;, \&quot;Paid\&quot;, \&quot;Partial\&quot;, \&quot;Void\&quot;

    :param updated_after: 
    :type updated_after: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: 
    :type sort: str
    :param company_idfk: 
    :type company_idfk: int

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def invoice_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Invoice by Invoice ID

    

    :param id: Invoice Transaction ID number
    :type id: int

    """
    return web.Response(status=200)


async def invoice_post(request: web.Request, model) -> web.Response:
    """Create a new draft invoice

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewInvoice.from_dict(model)
    return web.Response(status=200)
