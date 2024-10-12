from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.org_response import OrgResponse
from openapi_server import util


async def org_get(request: web.Request, ) -> web.Response:
    """Gets the current organisation

    Returns the current organisation info.


    """
    return web.Response(status=200)
