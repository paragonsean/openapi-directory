from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.get_one_invoice_emails200_response import GetOneInvoiceEmails200Response
from openapi_server import util


async def get_one_invoice_emails(request: web.Request, invoice_id, email_id) -> web.Response:
    """Get an invoice emails

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str
    :param email_id: 
    :type email_id: str
    :type email_id: str

    """
    return web.Response(status=200)
