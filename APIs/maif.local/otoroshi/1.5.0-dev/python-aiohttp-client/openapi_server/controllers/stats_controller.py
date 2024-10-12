from typing import List, Dict
from aiohttp import web

from openapi_server.models.stats import Stats
from openapi_server import util


async def global_live_stats(request: web.Request, ) -> web.Response:
    """Get global otoroshi stats

    Get global otoroshi stats


    """
    return web.Response(status=200)


async def service_live_stats(request: web.Request, id) -> web.Response:
    """Get live feed of otoroshi stats

    Get live feed of global otoroshi stats (global) or for a service {id}

    :param id: The service id or global for otoroshi stats
    :type id: str

    """
    return web.Response(status=200)
