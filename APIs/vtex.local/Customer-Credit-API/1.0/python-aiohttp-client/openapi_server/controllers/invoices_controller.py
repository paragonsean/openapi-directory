from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_invoice_request1 import ChangeInvoiceRequest1
from openapi_server.models.getinvoicesfromacheckingaccount1 import Getinvoicesfromacheckingaccount1
from openapi_server.models.markaninvoiceas_paid_request1 import MarkaninvoiceasPaidRequest1
from openapi_server.models.paidinvoices1 import Paidinvoices1
from openapi_server.models.postponeaninvoice_request1 import PostponeaninvoiceRequest1
from openapi_server.models.retrievedinvoice1 import Retrievedinvoice1
from openapi_server import util


async def cancel_invoice(request: web.Request, content_type, accept, credit_account_id, invoice_id) -> web.Response:
    """Cancel Invoice

    Changes invoice&#39;s status from ancells invoice by specified Id.

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param invoice_id: 
    :type invoice_id: str

    """
    return web.Response(status=200)


async def change_invoice(request: web.Request, credit_account_id, invoice_id, accept, content_type, body, friendly_id=None) -> web.Response:
    """Change Invoice

    Updates invoice&#39;s attributes &#x60;status&#x60;, &#x60;paymentLink&#x60; and &#x60;observation&#x60;.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param invoice_id: 
    :type invoice_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes
    :param friendly_id: Invoice&#39;s identification
    :type friendly_id: str

    """
    body = ChangeInvoiceRequest1.from_dict(body)
    return web.Response(status=200)


async def markaninvoiceas_paid(request: web.Request, credit_account_id, invoice_id, accept, content_type, body) -> web.Response:
    """Mark an invoice as Paid

    Pay an invoice.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param invoice_id: 
    :type invoice_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = MarkaninvoiceasPaidRequest1.from_dict(body)
    return web.Response(status=200)


async def postponeaninvoice(request: web.Request, credit_account_id, invoice_id, accept, content_type, body) -> web.Response:
    """Postpone an invoice

    Postpone an invoice.

    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param invoice_id: 
    :type invoice_id: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostponeaninvoiceRequest1.from_dict(body)
    return web.Response(status=200)


async def retrieve_invoiceby_id(request: web.Request, content_type, accept, credit_account_id, invoice_id) -> web.Response:
    """Retrieve Invoice by Id

    Returns associated data for the specified Invoice Id, like status  and value, for example.

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param credit_account_id: Credit account&#39;s identification
    :type credit_account_id: str
    :param invoice_id: 
    :type invoice_id: str

    """
    return web.Response(status=200)


async def searchallinvoices(request: web.Request, content_type, accept, _from=None, to=None, created_date_from=None, created_date_to=None, value=None, status=None, friendly_id=None, credit_account_id=None) -> web.Response:
    """Search all invoices

    Returns all invoices according to the informed query params in the request.

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param _from: 
    :type _from: str
    :param to: 
    :type to: str
    :param created_date_from: 
    :type created_date_from: str
    :param created_date_to: 
    :type created_date_to: str
    :param value: Invoice&#39;s value. It must be completed with a decimal value.
    :type value: 
    :param status: Invoice&#39;s status. It must be completed with \&quot;Paid\&quot;, \&quot;Cancelled\&quot; or \&quot;Open\&quot; value.
    :type status: str
    :param friendly_id: Invoice&#39;s identifier
    :type friendly_id: str
    :param credit_account_id: Credit account&#39;s identifier
    :type credit_account_id: str

    """
    return web.Response(status=200)


async def searchallinvoicesofa_account(request: web.Request, content_type, accept, credit_account_id) -> web.Response:
    """Retrieve invoice by creditAccountId

    Returns associated invoices by specified creditAccountId, the param that identifies a client in VTEX&#39;s system.

    :param content_type: The Media type of the body of the request. Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param credit_account_id: 
    :type credit_account_id: str

    """
    return web.Response(status=200)
