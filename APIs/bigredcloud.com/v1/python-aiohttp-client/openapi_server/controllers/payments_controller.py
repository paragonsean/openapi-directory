from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_payment_dto import BatchItemPaymentDto
from openapi_server.models.page_result_payment_query_dto import PageResultPaymentQueryDto
from openapi_server.models.payment_dto import PaymentDto
from openapi_server import util


async def payments_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Payment.

    

    :param id: Id of Payment to remove.
    :type id: int
    :param timestamp: Timestamp of Payment to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def payments_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def payments_post(request: web.Request, body) -> web.Response:
    """Creates a new Payment.

    

    :param body: Information of Payment to create.
    :type body: dict | bytes

    """
    body = PaymentDto.from_dict(body)
    return web.Response(status=200)


async def payments_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Payments.

    

    :param body: Batch of Payments to process.
    :type body: list | bytes

    """
    body = [BatchItemPaymentDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def payments_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Payment.

    

    :param id: Id of Payment to update.
    :type id: int
    :param body: Information of Payment to update.
    :type body: dict | bytes

    """
    body = PaymentDto.from_dict(body)
    return web.Response(status=200)


async def v1_payments_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Payments.

    

    :param id: Id of Payment to return.
    :type id: int

    """
    return web.Response(status=200)
