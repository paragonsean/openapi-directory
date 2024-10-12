from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_book_tran_type_dto import PageResultBookTranTypeDto
from openapi_server import util


async def book_tran_types_get(request: web.Request, ) -> web.Response:
    """Returns a list of global Book Transactions&#39; Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)
