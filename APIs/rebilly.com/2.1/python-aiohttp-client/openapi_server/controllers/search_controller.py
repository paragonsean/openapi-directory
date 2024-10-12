from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.search import Search
from openapi_server import util


async def get_search(request: web.Request, organization_id=None, sort=None, limit=None, offset=None, q=None) -> web.Response:
    """Search merchant data

    Search merchant&#39;s data to return resources such as customers, invoices, orders, transactions. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param q: The default search. It will search across resources and many fields.
    :type q: str

    """
    return web.Response(status=200)
