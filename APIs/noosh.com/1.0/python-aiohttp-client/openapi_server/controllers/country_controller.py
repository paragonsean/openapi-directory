from typing import List, Dict
from aiohttp import web

from openapi_server.models.country_list_vo import CountryListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server import util


async def get_country_list(request: web.Request, ) -> web.Response:
    """List all countries

    List all countries


    """
    return web.Response(status=200)
