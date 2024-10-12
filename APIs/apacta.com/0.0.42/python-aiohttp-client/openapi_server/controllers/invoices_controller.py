from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.integrations_products_sync_get200_response import IntegrationsProductsSyncGet200Response
from openapi_server.models.invoices_get200_response import InvoicesGet200Response
from openapi_server.models.invoices_invoice_id_get200_response import InvoicesInvoiceIdGet200Response
from openapi_server.models.invoices_invoice_id_put_request import InvoicesInvoiceIdPutRequest
from openapi_server.models.invoices_post_request import InvoicesPostRequest
from openapi_server import util


async def bulk_delete_invoices(request: web.Request, body) -> web.Response:
    """Bulk delete invoices

    

    :param body: Invoices ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def invoices_get(request: web.Request, contact_id=None, project_id=None, invoice_number=None, offer_number=None, is_draft=None, is_offer=None, is_locked=None, is_fixed_price=None, date_from=None, date_to=None, issued_date=None, sent_as_draft=None) -> web.Response:
    """View list of invoices

    

    :param contact_id: Used to filter on the &#x60;contact_id&#x60; of the invoices
    :type contact_id: str
    :type contact_id: str
    :param project_id: Used to filter on the &#x60;project_id&#x60; of the invoices
    :type project_id: str
    :type project_id: str
    :param invoice_number: Used to filter on the &#x60;invoice_number&#x60; of the invoices
    :type invoice_number: str
    :param offer_number: 
    :type offer_number: str
    :param is_draft: 
    :type is_draft: int
    :param is_offer: 
    :type is_offer: int
    :param is_locked: 
    :type is_locked: int
    :param is_fixed_price: 
    :type is_fixed_price: int
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param issued_date: 
    :type issued_date: str
    :param sent_as_draft: Used to filter invoices which are sent as draft to integration
    :type sent_as_draft: int

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    issued_date = util.deserialize_date(issued_date)
    return web.Response(status=200)


async def invoices_invoice_id_copy_post(request: web.Request, invoice_id, project_id=None, contact_id=None) -> web.Response:
    """Create a copy of an invoice

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str
    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param contact_id: 
    :type contact_id: str
    :type contact_id: str

    """
    return web.Response(status=200)


async def invoices_invoice_id_delete(request: web.Request, invoice_id) -> web.Response:
    """Delete invoice

    

    :param invoice_id: 
    :type invoice_id: str

    """
    return web.Response(status=200)


async def invoices_invoice_id_get(request: web.Request, invoice_id) -> web.Response:
    """View invoice

    

    :param invoice_id: 
    :type invoice_id: str

    """
    return web.Response(status=200)


async def invoices_invoice_id_link_project_pdf_post(request: web.Request, invoice_id) -> web.Response:
    """Creates an invoice file containing the project&#39;s pdf overview

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str

    """
    return web.Response(status=200)


async def invoices_invoice_id_put(request: web.Request, invoice_id, body=None) -> web.Response:
    """Edit invoice

    

    :param invoice_id: 
    :type invoice_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvoicesInvoiceIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def invoices_invoice_id_unlink_project_pdf_post(request: web.Request, invoice_id) -> web.Response:
    """Deletes the linked project overview pdf

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str

    """
    return web.Response(status=200)


async def invoices_post(request: web.Request, body=None) -> web.Response:
    """Add invoice

    

    :param body: 
    :type body: dict | bytes

    """
    body = InvoicesPostRequest.from_dict(body)
    return web.Response(status=200)


async def invoices_vat_options_get(request: web.Request, ) -> web.Response:
    """List VAT options

    


    """
    return web.Response(status=200)
