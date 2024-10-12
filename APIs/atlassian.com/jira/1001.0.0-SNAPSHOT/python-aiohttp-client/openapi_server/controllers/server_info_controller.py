from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_information import ServerInformation
from openapi_server import util


async def get_server_info(request: web.Request, ) -> web.Response:
    """Get Jira instance info

    Returns information about the Jira instance.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.


    """
    return web.Response(status=200)
