from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_books200_response import GetBooks200Response
from openapi_server import util


async def get_books(request: web.Request, ) -> web.Response:
    """List all books

    


    """
    return web.Response(status=200)
