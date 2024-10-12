from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_get200_response import SearchGet200Response
from openapi_server import util


async def search_get(request: web.Request, q) -> web.Response:
    """List all company ESG Ratings

    

    :param q: Company name or stock symbol
    :type q: str

    """
    return web.Response(status=200)
