from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_categories(request: web.Request, ) -> web.Response:
    """Get categories!

    &lt;p&gt;This operation provides a list of categories.&lt;/p&gt;


    """
    return web.Response(status=200)
