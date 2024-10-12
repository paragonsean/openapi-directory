from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.suggest_response import SuggestResponse
from openapi_server import util


async def suggest_post(request: web.Request, ) -> web.Response:
    """Submit a suggestion to improve a translation

    


    """
    return web.Response(status=200)
