from typing import List, Dict
from aiohttp import web

from openapi_server.models.wl_status_group import WlStatusGroup
from openapi_server import util


async def status_report_get(request: web.Request, ) -> web.Response:
    """Get status_report

    Get list of status reports from all status groups


    """
    return web.Response(status=200)
