from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def list_naics_get(request: web.Request, ) -> web.Response:
    """This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles

    &lt;p&gt;This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles. It takes no parameters.&lt;/p&gt;


    """
    return web.Response(status=200)
