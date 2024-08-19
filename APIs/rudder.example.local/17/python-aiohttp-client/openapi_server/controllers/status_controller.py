from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def call_none(request: web.Request, ) -> web.Response:
    """Check if Rudder is alive

    An unauthenticated API to check if Rudder web application is up and running. Be careful: this API does not follow other Rudder&#39;s API convention:  - it is not versioned, so the path is just &#x60;/api/status&#x60;; - it returns a plain text message.


    """
    return web.Response(status=200)
