from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_purchase_dto import BatchItemPurchaseDto
from openapi_server.models.page_result_purchase_query_dto import PageResultPurchaseQueryDto
from openapi_server.models.purchase_dto import PurchaseDto
from openapi_server import util


async def purchases_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Purchase.

    

    :param id: Id of Purchase to remove.
    :type id: int
    :param timestamp: Timestamp of Purchase to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def purchases_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Purchases. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def purchases_post(request: web.Request, body) -> web.Response:
    """Creates a new Purchase.

    

    :param body: Information of Purchase to create.
    :type body: dict | bytes

    """
    body = PurchaseDto.from_dict(body)
    return web.Response(status=200)


async def purchases_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Purchases.

    

    :param body: Batch of Purchases to process.
    :type body: list | bytes

    """
    body = [BatchItemPurchaseDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def purchases_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Purchase.

    

    :param id: Id of Purchase to update.
    :type id: int
    :param body: Information of Purchase to update.
    :type body: dict | bytes

    """
    body = PurchaseDto.from_dict(body)
    return web.Response(status=200)


async def v1_purchases_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Purchases.

    

    :param id: Id of Purchase to return.
    :type id: int

    """
    return web.Response(status=200)
