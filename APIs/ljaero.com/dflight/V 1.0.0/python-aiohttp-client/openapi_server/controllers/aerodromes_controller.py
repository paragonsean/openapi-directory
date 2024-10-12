from typing import List, Dict
from aiohttp import web

from openapi_server.models.aerodrome_distance_response import AerodromeDistanceResponse
from openapi_server.models.aerodrome_poly_response import AerodromePolyResponse
from openapi_server.models.aerodrome_route_response import AerodromeRouteResponse
from openapi_server.models.aerodromes_by_distance import AerodromesByDistance
from openapi_server.models.aerodromes_by_polygon import AerodromesByPolygon
from openapi_server.models.aerodromes_by_route import AerodromesByRoute
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def aerodromes_by_distance_us_v1_aerodromes_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve aerodromes within given distance of location.

    Retrieve aerodromes within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = AerodromesByDistance.from_dict(body)
    return web.Response(status=200)


async def aerodromes_by_poly_us_v1_aerodromes_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve aerodromes located within given area.

    Retrieve aerodromes located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = AerodromesByPolygon.from_dict(body)
    return web.Response(status=200)


async def aerodromes_by_route_us_v1_aerodromes_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve aerodromes found along a route.

    Retrieve aerodromes found along a route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.  Successful requests return a GeoJSON FeatureCollection, with a separate Feature for each Aerodrome found. All Features will include properties for the facility name, ident, type, and operational status.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = AerodromesByRoute.from_dict(body)
    return web.Response(status=200)
