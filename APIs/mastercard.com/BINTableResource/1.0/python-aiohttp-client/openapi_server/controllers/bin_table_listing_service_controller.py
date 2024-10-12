from typing import List, Dict
from aiohttp import web

from openapi_server.models.bin_table_response import BinTableResponse
from openapi_server.models.no_resource import NoResource
from openapi_server import util


async def binlisting_get(request: web.Request, ) -> web.Response:
    """BIN Table Listing file

    REST service will retrieve and return the BIN Table file to Merchants.


    """
    return web.Response(status=200)
