from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def v1_charitygeolocation_post(request: web.Request, ein=None) -> web.Response:
    """Get details!

    &lt;p&gt;This operation detail data.&lt;/p&gt;

    :param ein: ein (Employer Identification Number)
    :type ein: str

    """
    return web.Response(status=200)
