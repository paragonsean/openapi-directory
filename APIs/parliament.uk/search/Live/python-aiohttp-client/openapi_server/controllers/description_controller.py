from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def description_get(request: web.Request, ) -> web.Response:
    """OpenSearch description document

    


    """
    return web.Response(status=200)
