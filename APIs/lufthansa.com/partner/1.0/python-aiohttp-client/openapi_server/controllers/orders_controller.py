from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def orders(request: web.Request, order_id, accept, name) -> web.Response:
    """Orders

    Retrieve order by ID and optionally name. This service is only accessible for LH privileged partners

    :param order_id: Unique order identifier
    :type order_id: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param name: Surname of traveller
    :type name: str

    """
    return web.Response(status=200)
