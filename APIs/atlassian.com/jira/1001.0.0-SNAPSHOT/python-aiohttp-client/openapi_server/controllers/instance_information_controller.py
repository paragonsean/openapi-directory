from typing import List, Dict
from aiohttp import web

from openapi_server.models.license import License
from openapi_server import util


async def get_license(request: web.Request, ) -> web.Response:
    """Get license

    Returns licensing information about the Jira instance.  **[Permissions](#permissions) required:** None.


    """
    return web.Response(status=200)
