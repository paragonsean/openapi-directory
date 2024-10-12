from typing import List, Dict
from aiohttp import web

from openapi_server.models.creative_commons import CreativeCommons
from openapi_server import util


async def get_cc_licenses(request: web.Request, ) -> web.Response:
    """Get all Creative Commons licenses

    


    """
    return web.Response(status=200)
