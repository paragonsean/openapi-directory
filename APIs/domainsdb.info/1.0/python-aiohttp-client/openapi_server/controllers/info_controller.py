from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key_info import APIKeyInfo
from openapi_server.models.zone_info import ZoneInfo
from openapi_server.models.zone_stats import ZoneStats
from openapi_server import util


async def get_api_info_item(request: web.Request, api_key=None) -> web.Response:
    """get_api_info_item

    

    :param api_key: API key
    :type api_key: str

    """
    return web.Response(status=200)


async def get_statistics_collection(request: web.Request, page=None, limit=None) -> web.Response:
    """Returns overall stagtistics

    

    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int

    """
    return web.Response(status=200)


async def get_statistics_item(request: web.Request, zone, page=None, limit=None) -> web.Response:
    """Returns statistics for specific zone

    

    :param zone: 
    :type zone: str
    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int

    """
    return web.Response(status=200)


async def info_tld_get(request: web.Request, ) -> web.Response:
    """Returns overall Tld info

    


    """
    return web.Response(status=200)


async def info_tld_zone_get(request: web.Request, zone, page=None, limit=None) -> web.Response:
    """Returns statistics for specific zone

    

    :param zone: 
    :type zone: str
    :param page: Search page to request
    :type page: str
    :param limit: Results per page
    :type limit: int

    """
    return web.Response(status=200)
