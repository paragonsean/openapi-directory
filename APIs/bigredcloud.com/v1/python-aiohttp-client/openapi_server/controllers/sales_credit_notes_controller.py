from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_sales_invoice_credit_note_dto import BatchItemSalesInvoiceCreditNoteDto
from openapi_server.models.page_result_sales_credit_note_query_dto import PageResultSalesCreditNoteQueryDto
from openapi_server.models.sales_invoice_credit_note_dto import SalesInvoiceCreditNoteDto
from openapi_server import util


async def sales_credit_notes_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Sales Credit Note.

    

    :param id: Id of Sales Credit Note to remove.
    :type id: int
    :param timestamp: Timestamp of Sales Credit Note to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def sales_credit_notes_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def sales_credit_notes_post(request: web.Request, body) -> web.Response:
    """Creates a new Sales Credit Note.

    

    :param body: Information of Sales Credit Note to create.
    :type body: dict | bytes

    """
    body = SalesInvoiceCreditNoteDto.from_dict(body)
    return web.Response(status=200)


async def sales_credit_notes_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Sales Credit Notes.

    

    :param body: Batch of Sales Credit Notes to process.
    :type body: list | bytes

    """
    body = [BatchItemSalesInvoiceCreditNoteDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_credit_notes_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Sales Credit Note.

    

    :param id: Id of Sales Credit Note to update.
    :type id: int
    :param body: Information of Sales Credit Note to update.
    :type body: dict | bytes

    """
    body = SalesInvoiceCreditNoteDto.from_dict(body)
    return web.Response(status=200)


async def v1_sales_credit_notes_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Sales Credit Note.

    

    :param id: Id of Sales Credit Note to return.
    :type id: int

    """
    return web.Response(status=200)
