from typing import List, Dict
from aiohttp import web

from openapi_server.models.area_jo import AreaJO
from openapi_server import util


async def get_area(request: web.Request, area_uid, expand=None) -> web.Response:
    """Get area by UID.

    Search for a specific area by UID.

    :param area_uid: The Area UID 
    :type area_uid: str
    :param expand: Expand Provider
    :type expand: str

    """
    return web.Response(status=200)


async def list_areas(request: web.Request, lat=None, lon=None, radius=None, offset=None, limit=None, expand=None, type=None, provider=None, providernetwork=None) -> web.Response:
    """List Areas by Criteria.

    Search for areas (locations of rental objects) by criteria.

    :param lat: 
    :type lat: float
    :param lon: 
    :type lon: float
    :param radius: 
    :type radius: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int
    :param expand: 
    :type expand: str
    :param type: 
    :type type: str
    :param provider: 
    :type provider: str
    :param providernetwork: 
    :type providernetwork: str

    """
    return web.Response(status=200)
