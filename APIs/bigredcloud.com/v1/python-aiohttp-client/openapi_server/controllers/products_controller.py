from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_product_dto import BatchItemProductDto
from openapi_server.models.page_result_product_dto import PageResultProductDto
from openapi_server.models.product_dto import ProductDto
from openapi_server import util


async def products_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Product.

    

    :param id: Id of Product to remove.
    :type id: int
    :param timestamp: Timestamp of Product to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def products_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Products. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;stockCode\&quot; fields.

    


    """
    return web.Response(status=200)


async def products_post(request: web.Request, body) -> web.Response:
    """Creates a new Product.

    

    :param body: Information of Product to create.
    :type body: dict | bytes

    """
    body = ProductDto.from_dict(body)
    return web.Response(status=200)


async def products_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Products.

    

    :param body: Batch of Products to process.
    :type body: list | bytes

    """
    body = [BatchItemProductDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def products_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Product.

    

    :param id: Id of Product to update.
    :type id: int
    :param body: Information of Product to update.
    :type body: dict | bytes

    """
    body = ProductDto.from_dict(body)
    return web.Response(status=200)


async def v1_products_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Product.

    

    :param id: Id of Product to return.
    :type id: int

    """
    return web.Response(status=200)
