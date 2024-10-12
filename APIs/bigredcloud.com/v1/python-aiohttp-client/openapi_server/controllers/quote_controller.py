from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_item_quote_dto import BatchItemQuoteDto
from openapi_server.models.page_result_quote_dto import PageResultQuoteDto
from openapi_server.models.quote_dto import QuoteDto
from openapi_server.models.quote_generating_invoice_dto import QuoteGeneratingInvoiceDto
from openapi_server import util


async def quote_close(request: web.Request, id) -> web.Response:
    """Close a Quote.

    

    :param id: Id of Quote to close
    :type id: int

    """
    return web.Response(status=200)


async def quote_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Quote.

    

    :param id: Id of Quote to remove.
    :type id: int
    :param timestamp: Timestamp of Quote to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def quote_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Quotes.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.

    


    """
    return web.Response(status=200)


async def quote_post(request: web.Request, body) -> web.Response:
    """Creates a new Quote.

    

    :param body: Information of Quote to create.
    :type body: dict | bytes

    """
    body = QuoteDto.from_dict(body)
    return web.Response(status=200)


async def quote_post_create_quote_with_generating_reference(request: web.Request, body) -> web.Response:
    """Creates a new Quote with auto generating reference.

    

    :param body: Information of Quote to create.
    :type body: dict | bytes

    """
    body = QuoteDto.from_dict(body)
    return web.Response(status=200)


async def quote_post_generate_sale_invoice(request: web.Request, body) -> web.Response:
    """Generate a sale invoice from a Quote.  When sale invoice is empty, new sale invoice will be generated from Quote.

    

    :param body: Id of Quote to generate
    :type body: dict | bytes

    """
    body = QuoteGeneratingInvoiceDto.from_dict(body)
    return web.Response(status=200)


async def quote_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Quote.

    

    :param body: Batch of Quote to process.
    :type body: list | bytes

    """
    body = [BatchItemQuoteDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def quote_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Quote.

    

    :param id: Id of Quote to update.
    :type id: int
    :param body: Information of Quote to update.
    :type body: dict | bytes

    """
    body = QuoteDto.from_dict(body)
    return web.Response(status=200)


async def quote_reopen(request: web.Request, id) -> web.Response:
    """Reopen a Quote.

    

    :param id: Id of Quote to reopen
    :type id: int

    """
    return web.Response(status=200)


async def v1_quotes_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Quote.

    

    :param id: Id of Sale Rep to return.
    :type id: int

    """
    return web.Response(status=200)
