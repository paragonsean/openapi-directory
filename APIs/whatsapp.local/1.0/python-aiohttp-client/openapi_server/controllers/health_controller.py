from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def check_health(request: web.Request, ) -> web.Response:
    """Check-Health

    


    """
    return web.Response(status=200)


async def get_app_stats(request: web.Request, format=None) -> web.Response:
    """Get-App-Stats

    

    :param format: 
    :type format: str

    """
    return web.Response(status=200)


async def get_db_stats(request: web.Request, format=None) -> web.Response:
    """Get-DB-Stats

    

    :param format: 
    :type format: str

    """
    return web.Response(status=200)


async def get_metrics(request: web.Request, format=None) -> web.Response:
    """Get-Metrics (since v2.21.3)

    

    :param format: 
    :type format: str

    """
    return web.Response(status=200)


async def get_support_info(request: web.Request, ) -> web.Response:
    """Get-Support-Info

    


    """
    return web.Response(status=200)
