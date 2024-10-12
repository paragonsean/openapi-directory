from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server import util


async def domains_get(request: web.Request, ) -> web.Response:
    """Shop Domains

    Zalando API Domains Schema


    """
    return web.Response(status=200)
