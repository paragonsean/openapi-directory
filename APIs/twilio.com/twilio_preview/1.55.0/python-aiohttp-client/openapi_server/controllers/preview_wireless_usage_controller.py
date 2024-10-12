from typing import List, Dict
from aiohttp import web

from openapi_server.models.preview_wireless_sim_usage import PreviewWirelessSimUsage
from openapi_server import util


async def fetch_wireless_usage(request: web.Request, sim_sid, end=None, start=None) -> web.Response:
    """fetch_wireless_usage

    

    :param sim_sid: 
    :type sim_sid: str
    :param end: 
    :type end: str
    :param start: 
    :type start: str

    """
    return web.Response(status=200)
