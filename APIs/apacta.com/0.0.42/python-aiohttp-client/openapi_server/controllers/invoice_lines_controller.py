from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.invoice_lines_get200_response import InvoiceLinesGet200Response
from openapi_server.models.invoice_lines_invoice_line_id_get200_response import InvoiceLinesInvoiceLineIdGet200Response
from openapi_server.models.invoice_lines_invoice_line_id_put_request import InvoiceLinesInvoiceLineIdPutRequest
from openapi_server.models.invoice_lines_post_request import InvoiceLinesPostRequest
from openapi_server import util


async def invoice_line_texts_invoice_line_text_id_post(request: web.Request, invoice_line_text_id, html, image=None) -> web.Response:
    """Edit invoice line text

    

    :param invoice_line_text_id: Automatically added
    :type invoice_line_text_id: str
    :param html: 
    :type html: str
    :param image: 
    :type image: str

    """
    return web.Response(status=200)


async def invoice_line_texts_post(request: web.Request, html, invoice_id, image=None, placement=None) -> web.Response:
    """Add invoice line text

    

    :param html: 
    :type html: str
    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str
    :param image: 
    :type image: str
    :param placement: 
    :type placement: int

    """
    return web.Response(status=200)


async def invoice_lines_get(request: web.Request, invoice_id=None, product_id=None, user_id=None, name=None, discount_text=None) -> web.Response:
    """View list of invoice lines

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str
    :param product_id: 
    :type product_id: str
    :type product_id: str
    :param user_id: 
    :type user_id: str
    :type user_id: str
    :param name: 
    :type name: str
    :param discount_text: 
    :type discount_text: str

    """
    return web.Response(status=200)


async def invoice_lines_invoice_line_id_delete(request: web.Request, invoice_line_id) -> web.Response:
    """Delete invoice line

    

    :param invoice_line_id: 
    :type invoice_line_id: str
    :type invoice_line_id: str

    """
    return web.Response(status=200)


async def invoice_lines_invoice_line_id_get(request: web.Request, invoice_line_id) -> web.Response:
    """View invoice line

    

    :param invoice_line_id: 
    :type invoice_line_id: str
    :type invoice_line_id: str

    """
    return web.Response(status=200)


async def invoice_lines_invoice_line_id_put(request: web.Request, invoice_line_id, body=None) -> web.Response:
    """Edit invoice line

    

    :param invoice_line_id: 
    :type invoice_line_id: str
    :type invoice_line_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceLinesInvoiceLineIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def invoice_lines_post(request: web.Request, body=None) -> web.Response:
    """Add invoice line

    

    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceLinesPostRequest.from_dict(body)
    return web.Response(status=200)
