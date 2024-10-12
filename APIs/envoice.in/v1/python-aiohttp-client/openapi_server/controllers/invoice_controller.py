from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_status_api_model import ChangeStatusApiModel
from openapi_server.models.invoice_category_api_model import InvoiceCategoryApiModel
from openapi_server.models.invoice_category_create_api_model import InvoiceCategoryCreateApiModel
from openapi_server.models.invoice_category_delete_api_model import InvoiceCategoryDeleteApiModel
from openapi_server.models.invoice_category_update_api_model import InvoiceCategoryUpdateApiModel
from openapi_server.models.invoice_create_api_model import InvoiceCreateApiModel
from openapi_server.models.invoice_delete_api_model import InvoiceDeleteApiModel
from openapi_server.models.invoice_full_details_api_model import InvoiceFullDetailsApiModel
from openapi_server.models.invoice_update_api_model import InvoiceUpdateApiModel
from openapi_server.models.invoice_uri_api_model import InvoiceUriApiModel
from openapi_server.models.list_result_invoice_category_api_model import ListResultInvoiceCategoryApiModel
from openapi_server.models.list_result_invoice_details_api_model import ListResultInvoiceDetailsApiModel
from openapi_server.models.send_invoice_to_accountant_api_model import SendInvoiceToAccountantApiModel
from openapi_server.models.send_invoice_to_client_api_model import SendInvoiceToClientApiModel
from openapi_server import util


async def api_invoice_allcategories_get(request: web.Request, x_auth_key, x_auth_secret, query=None) -> web.Response:
    """Return all invoice categories for the account

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def api_invoice_deletecategory_post(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing invoice category

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceCategoryDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def api_invoice_newcategory_post(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create an invoice category

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceCategoryCreateApiModel.from_dict(body)
    return web.Response(status=200)


async def api_invoice_updatecategory_post(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Update an existing invoice category

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceCategoryUpdateApiModel.from_dict(body)
    return web.Response(status=200)


async def invoice_api_all(request: web.Request, x_auth_key, x_auth_secret, query_options_page=None, query_options_page_size=None) -> web.Response:
    """Return all invoices for the account

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param query_options_page: 
    :type query_options_page: int
    :param query_options_page_size: 
    :type query_options_page_size: int

    """
    return web.Response(status=200)


async def invoice_api_change_status(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Change invoice status

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeStatusApiModel.from_dict(body)
    return web.Response(status=200)


async def invoice_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing invoice

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def invoice_api_details(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return invoice data

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def invoice_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create an invoice

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceCreateApiModel.from_dict(body)
    return web.Response(status=200)


async def invoice_api_pdf(request: web.Request, id, x_auth_key, x_auth_secret, signed_version=None) -> web.Response:
    """Return the PDF for the invoice

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param signed_version: 
    :type signed_version: bool

    """
    return web.Response(status=200)


async def invoice_api_send_to_accountant(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Send the provided invoice to the accountant

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendInvoiceToAccountantApiModel.from_dict(body)
    return web.Response(status=200)


async def invoice_api_send_to_client(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Send the provided invoice to the client

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendInvoiceToClientApiModel.from_dict(body)
    return web.Response(status=200)


async def invoice_api_status(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Retrieve the status of the invoice

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def invoice_api_update(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Update an existing invoice

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoiceUpdateApiModel.from_dict(body)
    return web.Response(status=200)


async def invoice_api_uri(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return the unique url to the client&#39;s invoice

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)
