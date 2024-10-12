from typing import List, Dict
from aiohttp import web

from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def map_map_get(request: web.Request, variable, datetime, tile_x=None, tile_y=None, tile_zoom=None, min_lat=None, min_lon=None, max_lat=None, max_lon=None, key=None) -> web.Response:
    """Returns PNG weather map for given area and variable

    ## PNG weather forecast maps for given area and variable  ### Area specification There are two ways to specify geographical area you need for your map: 1. Specify &#x60;X&#x60; and &#x60;Y&#x60; coordinates and zoom level &#x60;Z&#x60; of desired tile in &lt;a href&#x3D;\&quot;https://www.maptiler.com/google-maps-coordinates-tile-bounds-projection/\&quot; rel&#x3D;\&quot;nofollow\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Maps Tile notation&lt;/a&gt;. 2. Specify latitude and longitude bounds of the area you want to cover.  ### Notes * The resulting PNG maps are **always** in &lt;a href&#x3D;\&quot;https://epsg.io/3857\&quot; rel&#x3D;\&quot;nofollow\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Mercator projection (EPSG:3857)&lt;/a&gt;. * As Meteosource only covers areas between latitudes 80° and -80°, you can only request maps within these bounds, when specifying the latitude and longitude boundaries. When specifying the area using Google Maps Tile notation, the regions outside our supported latitudes will be fully transparent. * The finest resolution is not available for maps covering very large regions. The resulting map will be automatically downscaled in this case, to guarantee high-speed responses. * Weather maps are only supported for forecasts, not for archive data.

    :param variable: Name of the variable for your map. Available values are:  * &#x60;temperature&#x60;: Temperature 2 metres above ground * &#x60;feels_like_temperature&#x60;: Feels like temperature * &#x60;clouds&#x60;: Percentage of sky covered by clouds * &#x60;precipitation&#x60;: Total precipitation amount accumulated since last hour * &#x60;wind_speed&#x60;: Wind speed 10 metres above the ground * &#x60;wind_gust&#x60;: Wind gust speed * &#x60;pressure&#x60;: Atmospheric pressure at mean sea level * &#x60;humidity&#x60;: Relative humidity * &#x60;wave_height&#x60;: Wave height * &#x60;wave_period&#x60;: Wave period * &#x60;sea_temperature&#x60;: Sea temperature (available only for +-24 hours) * &#x60;air_quality&#x60;: Air quality index * &#x60;ozone_surface&#x60;: Ozone at surface level * &#x60;ozone_total&#x60;: Total column ozone * &#x60;no2&#x60;: Nitrogen dioxide at surface level * &#x60;pm2.5&#x60;: Particulate matter d &lt; 2.5 µm (PM2.5) 
    :type variable: str
    :param datetime: There are two ways to specify date and time for your map:  1. Datetime in &#x60;YYYY-MM-DDTHH:MM&#x60; format and &#x60;UTC&#x60; timezone, e.g. &#x60;2021-08-24T12:00&#x60; 2. Offset from current time in &#x60;[+-]&lt;minutes|hours|days&gt;&#x60; format, e.g. &#x60;+10minutes&#x60;, &#x60;-2hours&#x60; or &#x60;+1days&#x60; 
    :type datetime: str
    :param tile_x: The X coordinate of Google Maps tile
    :type tile_x: int
    :param tile_y: The Y coordinate of Google Maps tile
    :type tile_y: int
    :param tile_zoom: The zoom level of Google Maps tile
    :type tile_zoom: int
    :param min_lat: Minimal latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.2 
    :type min_lat: str
    :param min_lon: Minimal longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.2 
    :type min_lon: str
    :param max_lat: Maximal latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.2. 
    :type max_lat: str
    :param max_lon: Maximal longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.2 
    :type max_lon: str
    :param key: Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header.
    :type key: str

    """
    return web.Response(status=200)
