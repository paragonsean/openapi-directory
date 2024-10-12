from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_invoice_request import CancelInvoiceRequest
from openapi_server.models.cancel_invoice_response import CancelInvoiceResponse
from openapi_server.models.create_invoice_request import CreateInvoiceRequest
from openapi_server.models.create_invoice_response import CreateInvoiceResponse
from openapi_server.models.delete_invoice_response import DeleteInvoiceResponse
from openapi_server.models.get_invoice_response import GetInvoiceResponse
from openapi_server.models.list_invoices_response import ListInvoicesResponse
from openapi_server.models.publish_invoice_request import PublishInvoiceRequest
from openapi_server.models.publish_invoice_response import PublishInvoiceResponse
from openapi_server.models.search_invoices_request import SearchInvoicesRequest
from openapi_server.models.search_invoices_response import SearchInvoicesResponse
from openapi_server.models.update_invoice_request import UpdateInvoiceRequest
from openapi_server.models.update_invoice_response import UpdateInvoiceResponse
from openapi_server import util


async def cancel_invoice(request: web.Request, invoice_id, body) -> web.Response:
    """CancelInvoice

    Cancels an invoice. The seller cannot collect payments for  the canceled invoice.  You cannot cancel an invoice in the &#x60;DRAFT&#x60; state or in a terminal state: &#x60;PAID&#x60;, &#x60;REFUNDED&#x60;, &#x60;CANCELED&#x60;, or &#x60;FAILED&#x60;.

    :param invoice_id: The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.
    :type invoice_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CancelInvoiceRequest.from_dict(body)
    return web.Response(status=200)


async def create_invoice(request: web.Request, body) -> web.Response:
    """CreateInvoice

    Creates a draft [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice)  for an order created using the Orders API.  A draft invoice remains in your account and no action is taken.  You must publish the invoice before Square can process it (send it to the customer&#39;s email address or charge the customer’s card on file).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateInvoiceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_invoice(request: web.Request, invoice_id, version=None) -> web.Response:
    """DeleteInvoice

    Deletes the specified invoice. When an invoice is deleted, the  associated order status changes to CANCELED. You can only delete a draft  invoice (you cannot delete a published invoice, including one that is scheduled for processing).

    :param invoice_id: The ID of the invoice to delete.
    :type invoice_id: str
    :param version: The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete. If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or  [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).
    :type version: int

    """
    return web.Response(status=200)


async def get_invoice(request: web.Request, invoice_id) -> web.Response:
    """GetInvoice

    Retrieves an invoice by invoice ID.

    :param invoice_id: The ID of the invoice to retrieve.
    :type invoice_id: str

    """
    return web.Response(status=200)


async def list_invoices(request: web.Request, location_id, cursor=None, limit=None) -> web.Response:
    """ListInvoices

    Returns a list of invoices for a given location. The response  is paginated. If truncated, the response includes a &#x60;cursor&#x60; that you     use in a subsequent request to retrieve the next set of invoices.

    :param location_id: The ID of the location for which to list invoices.
    :type location_id: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint.  Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type cursor: str
    :param limit: The maximum number of invoices to return (200 is the maximum &#x60;limit&#x60;).  If not provided, the server uses a default limit of 100 invoices.
    :type limit: int

    """
    return web.Response(status=200)


async def publish_invoice(request: web.Request, invoice_id, body) -> web.Response:
    """PublishInvoice

    Publishes the specified draft invoice.   After an invoice is published, Square  follows up based on the invoice configuration. For example, Square  sends the invoice to the customer&#39;s email address, charges the customer&#39;s card on file, or does  nothing. Square also makes the invoice available on a Square-hosted invoice page.   The invoice &#x60;status&#x60; also changes from &#x60;DRAFT&#x60; to a status  based on the invoice configuration. For example, the status changes to &#x60;UNPAID&#x60; if  Square emails the invoice or &#x60;PARTIALLY_PAID&#x60; if Square charge a card on file for a portion of the  invoice amount.

    :param invoice_id: The ID of the invoice to publish.
    :type invoice_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = PublishInvoiceRequest.from_dict(body)
    return web.Response(status=200)


async def search_invoices(request: web.Request, body) -> web.Response:
    """SearchInvoices

    Searches for invoices from a location specified in  the filter. You can optionally specify customers in the filter for whom to  retrieve invoices. In the current implementation, you can only specify one location and  optionally one customer.  The response is paginated. If truncated, the response includes a &#x60;cursor&#x60;  that you use in a subsequent request to retrieve the next set of invoices.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchInvoicesRequest.from_dict(body)
    return web.Response(status=200)


async def update_invoice(request: web.Request, invoice_id, body) -> web.Response:
    """UpdateInvoice

    Updates an invoice by modifying fields, clearing fields, or both. For most updates, you can use a sparse  &#x60;Invoice&#x60; object to add fields or change values and use the &#x60;fields_to_clear&#x60; field to specify fields to clear.  However, some restrictions apply. For example, you cannot change the &#x60;order_id&#x60; or &#x60;location_id&#x60; field and you  must provide the complete &#x60;custom_fields&#x60; list to update a custom field. Published invoices have additional restrictions.

    :param invoice_id: The ID of the invoice to update.
    :type invoice_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateInvoiceRequest.from_dict(body)
    return web.Response(status=200)
