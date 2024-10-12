from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server.models.news_get200_response import NewsGet200Response
from openapi_server import util


async def news_get(request: web.Request, ) -> web.Response:
    """Get Fortnite News

    


    """
    return web.Response(status=200)
