from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_sale_reps_dto import BatchItemSaleRepsDto
from openapi_server.models.page_result_sale_reps_dto import PageResultSaleRepsDto
from openapi_server.models.sale_reps_dto import SaleRepsDto
from openapi_server import util


async def sales_rep_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Sale Rep.

    

    :param id: Id of Sale Rep to remove.
    :type id: int
    :param timestamp: Timestamp of Sale Rep to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def sales_rep_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s SaleRep.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.

    


    """
    return web.Response(status=200)


async def sales_rep_post(request: web.Request, body) -> web.Response:
    """Creates a new SaleRep.

    

    :param body: Information of Sale Rep to create.
    :type body: dict | bytes

    """
    body = SaleRepsDto.from_dict(body)
    return web.Response(status=200)


async def sales_rep_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Sale Rep.

    

    :param body: Batch of Sale Rep to process.
    :type body: list | bytes

    """
    body = [BatchItemSaleRepsDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_rep_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Sale Rep.

    

    :param id: Id of Sale Rep to update.
    :type id: int
    :param body: Information of Sale Rep to update.
    :type body: dict | bytes

    """
    body = SaleRepsDto.from_dict(body)
    return web.Response(status=200)


async def v1_sales_reps_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single SaleRep.

    

    :param id: Id of Sale Rep to return.
    :type id: int

    """
    return web.Response(status=200)
