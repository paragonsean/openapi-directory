from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_schema(request: web.Request, ) -> web.Response:
    """Get schema

    Get schema


    """
    return web.Response(status=200)


async def get_status(request: web.Request, ) -> web.Response:
    """Get status

    Get the current iPlayer business layer status. This tells the caller the status of the iPlayer data, but not necessarily the overall status of the website. In the future it might include the status of the dependent data services within the BBC.


    """
    return web.Response(status=200)
