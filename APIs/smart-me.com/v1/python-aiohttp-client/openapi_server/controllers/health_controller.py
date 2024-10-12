from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def health_get(request: web.Request, ) -> web.Response:
    """A method returning HTTP 200 OK when queried.              It is used by Kubernetes probes to determine whether the app is healthy.

    


    """
    return web.Response(status=200)
