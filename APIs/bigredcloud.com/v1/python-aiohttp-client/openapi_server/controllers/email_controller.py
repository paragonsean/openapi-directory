from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_quote_dto import EmailQuoteDto
from openapi_server.models.email_statement_dto import EmailStatementDto
from openapi_server.models.sales_invoice_email_info_dto import SalesInvoiceEmailInfoDto
from openapi_server import util


async def email_send_email_statement(request: web.Request, body) -> web.Response:
    """Sends a Statement email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.

    

    :param body: 
    :type body: dict | bytes

    """
    body = EmailStatementDto.from_dict(body)
    return web.Response(status=200)


async def email_send_quote(request: web.Request, body) -> web.Response:
    """Sends a Quote email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.

    

    :param body: 
    :type body: dict | bytes

    """
    body = EmailQuoteDto.from_dict(body)
    return web.Response(status=200)


async def email_send_sales_invoice(request: web.Request, body) -> web.Response:
    """Sends a Sales Invoice email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Sales Invoice Customer&#39;s address.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SalesInvoiceEmailInfoDto.from_dict(body)
    return web.Response(status=200)
