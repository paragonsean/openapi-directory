from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_account_dto import PageResultAccountDto
from openapi_server import util


async def accounts_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Accounts. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.

    


    """
    return web.Response(status=200)
