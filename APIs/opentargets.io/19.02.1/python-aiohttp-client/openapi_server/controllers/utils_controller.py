from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_data_metrics_0(request: web.Request, ) -> web.Response:
    """Get metrics about the current data release

    Returns the metrics about associations and evidences, divided by datasource, genes and so on. 


    """
    return web.Response(status=200)


async def get_data_stats_0(request: web.Request, ) -> web.Response:
    """Get statistics about the current data release

    Returns the number of associations and evidences, divided by datasource. 


    """
    return web.Response(status=200)


async def get_ping_0(request: web.Request, ) -> web.Response:
    """Ping service

    Check if the API is up 


    """
    return web.Response(status=200)


async def get_therapeutic_areas_0(request: web.Request, ) -> web.Response:
    """Get the list of therapeutic areas about the current data release

    Returns the list of therapeutic areas for the current data release 


    """
    return web.Response(status=200)


async def get_version_0(request: web.Request, ) -> web.Response:
    """Get API version

    Returns current API version. 


    """
    return web.Response(status=200)
