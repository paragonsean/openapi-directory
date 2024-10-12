from typing import List, Dict
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server import util


async def addons_list(request: web.Request, ) -> web.Response:
    """List all addons

     A paginated list of addons configurable with the OSF, for read purposes only. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 addons. Each resource in the array is a separate addon object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.


    """
    return web.Response(status=200)
