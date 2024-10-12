from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def getfeedorderstatus(request: web.Request, max_lot, accept, content_type) -> web.Response:
    """Get feed order status

    Get feed order status (deprecated)

    :param max_lot: 
    :type max_lot: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str

    """
    return web.Response(status=200)
