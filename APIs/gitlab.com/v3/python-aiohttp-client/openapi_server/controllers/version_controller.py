from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_v3_version(request: web.Request, ) -> web.Response:
    """Get the version information of the GitLab instance.

    This feature was introduced in GitLab 8.13.


    """
    return web.Response(status=200)
