from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_zone_result import MultiZoneResult
from openapi_server.models.zone_create import ZoneCreate
from openapi_server.models.zone_result import ZoneResult
from openapi_server import util


async def zone_get(request: web.Request, filters=None) -> web.Response:
    """get a list of zones

    Get all zones. possibly with filters 

    :param filters: A JSON encoded array of ZoneFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ZoneFilter will be included. 
    :type filters: str

    """
    return web.Response(status=200)


async def zone_post(request: web.Request, zone) -> web.Response:
    """create zone

    Create a new zone. 

    :param zone: the zone to create
    :type zone: dict | bytes

    """
    zone = ZoneCreate.from_dict(zone)
    return web.Response(status=200)


async def zone_zone_key_delete(request: web.Request, zone_key, checksum) -> web.Response:
    """delete zone

    Delete a zone. 

    :param zone_key: the zone key
    :type zone_key: str
    :param checksum: the current checksum of the zone to be deleted
    :type checksum: str

    """
    return web.Response(status=200)


async def zone_zone_key_get(request: web.Request, zone_key) -> web.Response:
    """get zone

    Get details for a single zone 

    :param zone_key: the zone key
    :type zone_key: str

    """
    return web.Response(status=200)
