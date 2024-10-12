from typing import List, Dict
from aiohttp import web

from openapi_server.models.thread_pool_info import ThreadPoolInfo
from openapi_server import util


async def utility_v1_health_heartbeat_get(request: web.Request, ) -> web.Response:
    """utility_v1_health_heartbeat_get

    


    """
    return web.Response(status=200)


async def utility_v1_health_threadinfo_get(request: web.Request, ) -> web.Response:
    """utility_v1_health_threadinfo_get

    


    """
    return web.Response(status=200)
