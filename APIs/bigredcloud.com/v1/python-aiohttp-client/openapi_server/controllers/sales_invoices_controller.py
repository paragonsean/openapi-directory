from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_sales_invoice_credit_note_dto import BatchItemSalesInvoiceCreditNoteDto
from openapi_server.models.page_result_sales_invoice_query_dto import PageResultSalesInvoiceQueryDto
from openapi_server.models.sales_invoice_credit_note_dto import SalesInvoiceCreditNoteDto
from openapi_server import util


async def sales_invoices_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Sales Invoice.

    

    :param id: Id of Sales Invoice to remove.
    :type id: int
    :param timestamp: Timestamp of Sales Invoice to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def sales_invoices_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Sales Invoices. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def sales_invoices_post(request: web.Request, body) -> web.Response:
    """Creates a new Sales Invoice.

    

    :param body: Information of Sales Invoice to create.
    :type body: dict | bytes

    """
    body = SalesInvoiceCreditNoteDto.from_dict(body)
    return web.Response(status=200)


async def sales_invoices_post_create_sale_invoice_with_generating_reference(request: web.Request, body) -> web.Response:
    """Creates a new Sale Invoice with auto generating reference.

    

    :param body: Information of Sale Invoice to create.
    :type body: dict | bytes

    """
    body = SalesInvoiceCreditNoteDto.from_dict(body)
    return web.Response(status=200)


async def sales_invoices_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Sales Invoices.

    

    :param body: Batch of Sales Invoices to process.
    :type body: list | bytes

    """
    body = [BatchItemSalesInvoiceCreditNoteDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_invoices_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Sales Invoice.

    

    :param id: Id of Sales Invoice to update.
    :type id: int
    :param body: Information of Sales Invoice to update.
    :type body: dict | bytes

    """
    body = SalesInvoiceCreditNoteDto.from_dict(body)
    return web.Response(status=200)


async def v1_sales_invoices_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Sales Invoice.

    

    :param id: Id of Sales Invoice to return.
    :type id: int

    """
    return web.Response(status=200)
