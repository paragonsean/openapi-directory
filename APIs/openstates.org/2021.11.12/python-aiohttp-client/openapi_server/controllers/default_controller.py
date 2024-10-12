from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def metrics_metrics_get(request: web.Request, ) -> web.Response:
    """Metrics

    Endpoint that serves Prometheus metrics.


    """
    return web.Response(status=200)
