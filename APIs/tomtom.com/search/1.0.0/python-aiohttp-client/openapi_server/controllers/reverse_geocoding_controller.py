from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_version_number_reverse_geocode_cross_street_position_ext_get(request: web.Request, version_number, position, ext, limit=None, spatial_keys=None, heading=None, radius=None, language=None) -> web.Response:
    """Cross Street lookup

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param position: This is specified as a comma separated string composed of lat., lon.
    :type position: str
    :param ext: Expected response format.
    :type ext: str
    :param limit: Maximum number of cross-streets to return.
    :type limit: int
    :param spatial_keys: If the \&quot;spatialKeys\&quot; flag is set, the response will also contain a proprietary geospatial keys for a specified location.
    :type spatial_keys: bool
    :param heading: The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    :type heading: float
    :param radius: The maximum distance in meters from the specified position for the reverse geocoder to consider.
    :type radius: int
    :param language: Language in which search results should be returned. Should be one of &lt;a href&#x3D;\&quot;/search-api/search-api-documentation/supported-languages\&quot;&gt;supported IETF language tags&lt;/a&gt;, case insensitive.
    :type language: str

    """
    return web.Response(status=200)


async def search_version_number_reverse_geocode_position_ext_get(request: web.Request, version_number, position, ext, spatial_keys=None, return_speed_limit=None, heading=None, radius=None, number=None, return_road_use=None, road_use=None, param_callback=None) -> web.Response:
    """Reverse Geocode

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param position: This is specified as a comma separated string composed of lat., lon.
    :type position: str
    :param ext: Expected response format.
    :type ext: str
    :param spatial_keys: If the \&quot;spatialKeys\&quot; flag is set, the response will also contain a proprietary geospatial keys for a specified location.
    :type spatial_keys: bool
    :param return_speed_limit: To enable return of the posted speed limit (where available).
    :type return_speed_limit: bool
    :param heading: The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    :type heading: float
    :param radius: The maximum distance in meters from the specified position for the reverse geocoder to consider.
    :type radius: int
    :param number: If a number is sent in along with the request, the response may include the side of the street (Left/Right) and an offset position for that number.
    :type number: str
    :param return_road_use: Enables return of the road use array for reverse geocodes at street level.
    :type return_road_use: bool
    :param road_use: Restricts reverse geocodes to a certain type of road use. The road use array for reverse geocodes can be one or more of: [\&quot;LimitedAccess\&quot;, \&quot;Arterial\&quot;, \&quot;Terminal\&quot;, \&quot;Ramp\&quot;, \&quot;Rotary\&quot;, \&quot;LocalStreet\&quot;].
    :type road_use: str
    :param param_callback: Specifies the jsonp callback method.
    :type param_callback: str

    """
    return web.Response(status=200)
