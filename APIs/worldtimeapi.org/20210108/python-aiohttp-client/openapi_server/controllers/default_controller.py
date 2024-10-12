from typing import List, Dict
from aiohttp import web

from openapi_server.models.date_time_json_response import DateTimeJsonResponse
from openapi_server.models.error_json_response import ErrorJsonResponse
from openapi_server import util


async def ip_get(request: web.Request, ) -> web.Response:
    """request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

    


    """
    return web.Response(status=200)


async def ip_ipv4_get(request: web.Request, ipv4) -> web.Response:
    """request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

    

    :param ipv4: 
    :type ipv4: str

    """
    return web.Response(status=200)


async def ip_ipv4_txt_get(request: web.Request, ipv4) -> web.Response:
    """request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

    

    :param ipv4: 
    :type ipv4: str

    """
    return web.Response(status=200)


async def ip_txt_get(request: web.Request, ) -> web.Response:
    """request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

    


    """
    return web.Response(status=200)


async def timezone_area_get(request: web.Request, area) -> web.Response:
    """a listing of all timezones available for that area.

    

    :param area: 
    :type area: str

    """
    return web.Response(status=200)


async def timezone_area_location_get(request: web.Request, area, location) -> web.Response:
    """request the current time for a timezone.

    

    :param area: 
    :type area: str
    :param location: 
    :type location: str

    """
    return web.Response(status=200)


async def timezone_area_location_region_get(request: web.Request, area, location, region) -> web.Response:
    """request the current time for a timezone.

    

    :param area: 
    :type area: str
    :param location: 
    :type location: str
    :param region: 
    :type region: str

    """
    return web.Response(status=200)


async def timezone_area_location_region_txt_get(request: web.Request, area, location, region) -> web.Response:
    """request the current time for a timezone.

    

    :param area: 
    :type area: str
    :param location: 
    :type location: str
    :param region: 
    :type region: str

    """
    return web.Response(status=200)


async def timezone_area_location_txt_get(request: web.Request, area, location) -> web.Response:
    """request the current time for a timezone.

    

    :param area: 
    :type area: str
    :param location: 
    :type location: str

    """
    return web.Response(status=200)


async def timezone_area_txt_get(request: web.Request, area) -> web.Response:
    """a listing of all timezones available for that area.

    

    :param area: 
    :type area: str

    """
    return web.Response(status=200)


async def timezone_get(request: web.Request, ) -> web.Response:
    """a listing of all timezones.

    


    """
    return web.Response(status=200)


async def timezone_txt_get(request: web.Request, ) -> web.Response:
    """a listing of all timezones.

    


    """
    return web.Response(status=200)
