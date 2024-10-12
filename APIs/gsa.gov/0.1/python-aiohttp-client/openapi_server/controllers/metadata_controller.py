from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def metadata_get(request: web.Request, ) -> web.Response:
    """This endpoint returns metadata for the most recent data loads of SAM and FPDS data

    &lt;p&gt;This endpoint returns metadata for the most recent data loads of SAM and FPDS data. It takes no parameters.&lt;/p&gt;


    """
    return web.Response(status=200)
