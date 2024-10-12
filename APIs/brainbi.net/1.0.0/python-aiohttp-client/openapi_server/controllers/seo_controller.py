from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def seo_latest_rankings(request: web.Request, =None) -> web.Response:
    """SEO Latest Rankings

    This resource lists all pricing rules that are currently saved in you account.

    :param : 
    :type : str

    """
    return web.Response(status=200)
