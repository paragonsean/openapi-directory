from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def chromecast_icon(request: web.Request, ) -> web.Response:
    """Chromecast Icon

    **Update:** This no longer exists. It&#39;s not useful, anyway.  A redirect to &#x60;http://www.gstatic.com/eureka/images/eureka_device.png&#x60;


    """
    return web.Response(status=200)


async def legal_notice(request: web.Request, ) -> web.Response:
    """Legal Notice

    All licenses of programs used by Home.


    """
    return web.Response(status=200)
