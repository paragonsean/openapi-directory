from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_invoice_in import EmailInvoiceIn
from openapi_server.models.email_invoice_out import EmailInvoiceOut
from openapi_server.models.email_refund_in import EmailRefundIn
from openapi_server.models.email_refund_out import EmailRefundOut
from openapi_server import util


async def email_invoice(request: web.Request, key, input) -> web.Response:
    """Email invoice

    

    :param key: Transaction key.
    :type key: str
    :param input: Input
    :type input: dict | bytes

    """
    input = EmailInvoiceIn.from_dict(input)
    return web.Response(status=200)


async def email_refund(request: web.Request, key, refund_note_number, input) -> web.Response:
    """Email credit note

    

    :param key: Transaction key.
    :type key: str
    :param refund_note_number: Refund note id.
    :type refund_note_number: str
    :param input: Input
    :type input: dict | bytes

    """
    input = EmailRefundIn.from_dict(input)
    return web.Response(status=200)
