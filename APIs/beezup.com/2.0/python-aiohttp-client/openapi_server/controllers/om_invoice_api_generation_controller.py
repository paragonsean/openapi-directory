from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.generate_batch_order_invoice_error_response_item import GenerateBatchOrderInvoiceErrorResponseItem
from openapi_server.models.generate_batch_order_invoice_request_item import GenerateBatchOrderInvoiceRequestItem
from openapi_server.models.generate_order_invoice_request import GenerateOrderInvoiceRequest
from openapi_server.models.generate_order_invoice_response import GenerateOrderInvoiceResponse
from openapi_server.models.get_order_invoice_pdf_from_html_invoice_url_request import GetOrderInvoicePdfFromHtmlInvoiceUrlRequest
from openapi_server.models.preview_order_invoice_request import PreviewOrderInvoiceRequest
from openapi_server.models.preview_order_invoice_response import PreviewOrderInvoiceResponse
from openapi_server import util


async def generate_batch_order_invoice(request: web.Request, user_name, body) -> web.Response:
    """Generate an Order Invoice batch

    

    :param user_name: Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login.
    :type user_name: str
    :param body: 
    :type body: list | bytes

    """
    body = [GenerateBatchOrderInvoiceRequestItem.from_dict(d) for d in body]
    return web.Response(status=200)


async def generate_order_invoice(request: web.Request, marketplace_technical_code, account_id, beez_up_order_uuid, user_name, body) -> web.Response:
    """Generate an Order Invoice

    

    :param marketplace_technical_code: The Marketplace Technical Code
    :type marketplace_technical_code: str
    :param account_id: The Account Identifier
    :type account_id: str
    :param beez_up_order_uuid: The BeezUP Order UUID
    :type beez_up_order_uuid: str
    :param user_name: Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login.
    :type user_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateOrderInvoiceRequest.from_dict(body)
    return web.Response(status=200)


async def get_order_invoice_pdf(request: web.Request, body) -> web.Response:
    """Returns the PDF version of the invoice

    

    :param body: 
    :type body: dict | bytes

    """
    body = GetOrderInvoicePdfFromHtmlInvoiceUrlRequest.from_dict(body)
    return web.Response(status=200)


async def get_order_invoice_preview(request: web.Request, marketplace_technical_code, account_id, beez_up_order_uuid, accept_encoding, body) -> web.Response:
    """View a preview an Order Invoice

    

    :param marketplace_technical_code: The Marketplace Technical Code
    :type marketplace_technical_code: str
    :param account_id: The Account Identifier
    :type account_id: str
    :param beez_up_order_uuid: The BeezUP Order UUID
    :type beez_up_order_uuid: str
    :param accept_encoding: Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
    :type accept_encoding: List[str]
    :param body: 
    :type body: dict | bytes

    """
    body = PreviewOrderInvoiceRequest.from_dict(body)
    return web.Response(status=200)
