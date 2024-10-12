from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.wx_by_distance import WxByDistance
from openapi_server.models.wx_by_polygon import WxByPolygon
from openapi_server.models.wx_by_route import WxByRoute
from openapi_server.models.wx_distance_response import WxDistanceResponse
from openapi_server.models.wx_poly_response import WxPolyResponse
from openapi_server.models.wx_route_response import WxRouteResponse
from openapi_server import util


async def wx_by_distance_us_v1_wx_forecast_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve forecast values within given distance of location for all requested weather elements and time periods.

    Retrieve forecast values for selected weather elements and time period. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000) * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = WxByDistance.from_dict(body)
    return web.Response(status=200)


async def wx_by_poly_us_v1_wx_forecast_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve forecast values within given GeoJSON polygon for all requested weather elements and time periods.

    Retrieve forecast values located within given area for requested weather elements and time period. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2. * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = WxByPolygon.from_dict(body)
    return web.Response(status=200)


async def wx_by_route_us_v1_wx_forecast_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve forecast values along a route for all requested weather elements and time periods.

    Retrieve forecast values along route for requested weather elements and time period. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km. * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = WxByRoute.from_dict(body)
    return web.Response(status=200)
