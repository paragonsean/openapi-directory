from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.invoice_line_text_template_get200_response import InvoiceLineTextTemplateGet200Response
from openapi_server.models.invoice_line_text_template_invoice_line_text_template_id_get200_response import InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response
from openapi_server import util


async def invoice_line_text_template_get(request: web.Request, ) -> web.Response:
    """Get a list of invoice line text templates

    


    """
    return web.Response(status=200)


async def invoice_line_text_template_invoice_line_text_template_id_delete(request: web.Request, invoice_line_text_template_id) -> web.Response:
    """Delete an invoice line text template

    

    :param invoice_line_text_template_id: 
    :type invoice_line_text_template_id: str
    :type invoice_line_text_template_id: str

    """
    return web.Response(status=200)


async def invoice_line_text_template_invoice_line_text_template_id_get(request: web.Request, invoice_line_text_template_id) -> web.Response:
    """Get a single invoice line text template

    

    :param invoice_line_text_template_id: 
    :type invoice_line_text_template_id: str
    :type invoice_line_text_template_id: str

    """
    return web.Response(status=200)


async def invoice_line_text_template_invoice_line_text_template_id_post(request: web.Request, invoice_line_text_template_id, html, image=None) -> web.Response:
    """Edit an invoice line text template

    

    :param invoice_line_text_template_id: 
    :type invoice_line_text_template_id: str
    :type invoice_line_text_template_id: str
    :param html: 
    :type html: str
    :param image: 
    :type image: str

    """
    return web.Response(status=200)


async def invoice_line_text_template_post(request: web.Request, html, image=None) -> web.Response:
    """Add a new invoice line text template

    

    :param html: 
    :type html: str
    :param image: 
    :type image: str

    """
    return web.Response(status=200)
