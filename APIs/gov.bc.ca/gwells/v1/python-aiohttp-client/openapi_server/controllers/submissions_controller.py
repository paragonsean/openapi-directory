from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def submissions_options_list(request: web.Request, ) -> web.Response:
    """submissions_options_list

    Options required for submitting activity report forms


    """
    return web.Response(status=200)
