from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def g_etv1_ping_format(request: web.Request, ) -> web.Response:
    """Returns whether the system is up.

    &lt;p&gt;Returns ‘pong’ if the site is up&lt;/p&gt; 


    """
    return web.Response(status=200)
