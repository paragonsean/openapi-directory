from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_prometheus_metrics(request: web.Request, ) -> web.Response:
    """Query server for exposed Prometheus metrics

    See Prometheus documentation for a complete data model.


    """
    return web.Response(status=200)
