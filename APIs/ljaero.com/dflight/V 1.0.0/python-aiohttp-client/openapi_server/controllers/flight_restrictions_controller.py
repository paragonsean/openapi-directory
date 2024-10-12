from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.notams_by_distance import NOTAMsByDistance
from openapi_server.models.notams_by_polygon import NOTAMsByPolygon
from openapi_server.models.notams_by_route import NOTAMsByRoute
from openapi_server.models.notams_distance_response import NOTAMsDistanceResponse
from openapi_server.models.notams_poly_response import NOTAMsPolyResponse
from openapi_server.models.notams_route_response import NOTAMsRouteResponse
from openapi_server import util


async def tfr_by_distance_us_v1_restrictions_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve flight restrictions applicable within given distance of location.

    Retrieve Flight Restrictions applicable within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = NOTAMsByDistance.from_dict(body)
    return web.Response(status=200)


async def tfr_by_poly_us_v1_restrictions_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve flight restrictions applicable within given area.

    Retrieve Flight Restrictions located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = NOTAMsByPolygon.from_dict(body)
    return web.Response(status=200)


async def tfr_by_route_us_v1_restrictions_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve flight restrictions applicable along route.

    Retrieve Flight Restrictions applicable along your route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = NOTAMsByRoute.from_dict(body)
    return web.Response(status=200)
