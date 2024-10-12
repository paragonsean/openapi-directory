from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_cash_receipt_dto import BatchItemCashReceiptDto
from openapi_server.models.cash_receipt_dto import CashReceiptDto
from openapi_server.models.page_result_cash_receipt_query_dto import PageResultCashReceiptQueryDto
from openapi_server import util


async def cash_receipts_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Cash Receipt.

    

    :param id: Id of Cash Receipt to remove.
    :type id: int
    :param timestamp: Timestamp of Cash Receipt to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def cash_receipts_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Cash Receipts. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def cash_receipts_post(request: web.Request, body) -> web.Response:
    """Creates a new Cash Receipt.

    

    :param body: Information of Cash Receipt to create.
    :type body: dict | bytes

    """
    body = CashReceiptDto.from_dict(body)
    return web.Response(status=200)


async def cash_receipts_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Cash Receipts.

    

    :param body: Batch of Cash Receipts to process.
    :type body: list | bytes

    """
    body = [BatchItemCashReceiptDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def cash_receipts_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Cash Receipt.

    

    :param id: Id of Cash Receipt to update.
    :type id: int
    :param body: Information of Cash Receipt to update.
    :type body: dict | bytes

    """
    body = CashReceiptDto.from_dict(body)
    return web.Response(status=200)


async def v1_cash_receipts_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Cash Receipt.

    

    :param id: Id of Cash Receipt to return.
    :type id: int

    """
    return web.Response(status=200)
