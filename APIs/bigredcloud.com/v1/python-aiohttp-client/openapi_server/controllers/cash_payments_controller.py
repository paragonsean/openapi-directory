from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_cash_payment_dto import BatchItemCashPaymentDto
from openapi_server.models.cash_payment_dto import CashPaymentDto
from openapi_server.models.page_result_cash_payment_query_dto import PageResultCashPaymentQueryDto
from openapi_server import util


async def cash_payments_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Cash Payment.

    

    :param id: Id of Cash Receipt to remove.
    :type id: int
    :param timestamp: Timestamp of Cash Receipt to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def cash_payments_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Cash Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def cash_payments_post(request: web.Request, body) -> web.Response:
    """Creates a new Cash Payment.

    

    :param body: Information of Cash Receipt to create.
    :type body: dict | bytes

    """
    body = CashPaymentDto.from_dict(body)
    return web.Response(status=200)


async def cash_payments_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Cash Payments.

    

    :param body: Batch of Cash Receipts to process.
    :type body: list | bytes

    """
    body = [BatchItemCashPaymentDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def cash_payments_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Cash Payment.

    

    :param id: Id of Cash Receipt to update.
    :type id: int
    :param body: Information of Cash Receipt to update.
    :type body: dict | bytes

    """
    body = CashPaymentDto.from_dict(body)
    return web.Response(status=200)


async def v1_cash_payments_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Cash Payment.

    

    :param id: Id of Cash Receipt to return.
    :type id: int

    """
    return web.Response(status=200)
