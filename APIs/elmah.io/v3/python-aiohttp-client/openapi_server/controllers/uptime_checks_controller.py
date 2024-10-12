from typing import List, Dict
from aiohttp import web

from openapi_server.models.uptime_check import UptimeCheck
from openapi_server import util


async def uptime_checks_get_all(request: web.Request, ) -> web.Response:
    """Fetch a list of uptime checks. Currently in closed beta. Get in contact to get access to this endpoint.

    Required permission: &#x60;uptimechecks_read&#x60;


    """
    return web.Response(status=200)
