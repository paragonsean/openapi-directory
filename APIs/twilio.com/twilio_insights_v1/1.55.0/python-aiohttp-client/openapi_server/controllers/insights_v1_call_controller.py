from typing import List, Dict
from aiohttp import web

from openapi_server.models.insights_v1_call import InsightsV1Call
from openapi_server import util


async def fetch_call(request: web.Request, sid) -> web.Response:
    """fetch_call

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)
