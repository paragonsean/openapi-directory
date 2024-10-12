from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def delete_authz_cache(request: web.Request, ) -> web.Response:
    """Clear cached authorization information

    Clears the node of cached authorization information for the current user.


    """
    return web.Response(status=200)
