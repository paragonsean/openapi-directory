from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_sales_entry_dto import BatchItemSalesEntryDto
from openapi_server.models.page_result_sales_entry_query_dto import PageResultSalesEntryQueryDto
from openapi_server.models.sales_entry_dto import SalesEntryDto
from openapi_server import util


async def sales_entries_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Sales Entry.

    

    :param id: Id of Sales Entry to remove.
    :type id: int
    :param timestamp: Timestamp of Sales Entry to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def sales_entries_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Sales Entries. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def sales_entries_post(request: web.Request, body) -> web.Response:
    """Creates a new Sales Entry.

    

    :param body: Information of Sales Entry to create.
    :type body: dict | bytes

    """
    body = SalesEntryDto.from_dict(body)
    return web.Response(status=200)


async def sales_entries_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Sales Entries.

    

    :param body: Batch of Sales Entries to process.
    :type body: list | bytes

    """
    body = [BatchItemSalesEntryDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def sales_entries_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Sales Entry.

    

    :param id: Id of Sales Entry to update.
    :type id: int
    :param body: Information of Sales Entry to update.
    :type body: dict | bytes

    """
    body = SalesEntryDto.from_dict(body)
    return web.Response(status=200)


async def v1_sales_entries_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Sales Entry.

    

    :param id: Id of Sales Entry to return.
    :type id: int

    """
    return web.Response(status=200)
