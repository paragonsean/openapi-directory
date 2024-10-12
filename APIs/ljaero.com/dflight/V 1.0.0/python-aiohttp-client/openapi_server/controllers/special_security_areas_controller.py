from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.ssaby_distance import SSAByDistance
from openapi_server.models.ssaby_polygon import SSAByPolygon
from openapi_server.models.ssaby_route import SSAByRoute
from openapi_server.models.ssa_distance_response import SSADistanceResponse
from openapi_server.models.ssa_poly_response import SSAPolyResponse
from openapi_server.models.ssa_route_response import SSARouteResponse
from openapi_server import util


async def ssa_by_distance_us_v1_ssa_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all special security areas located within given distance of location.

    Retrieve special security areas existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = SSAByDistance.from_dict(body)
    return web.Response(status=200)


async def ssa_by_poly_us_v1_ssa_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all special security areas located within given GeoJSON Polygon.

    Retrieve all special security areas located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = SSAByPolygon.from_dict(body)
    return web.Response(status=200)


async def ssa_by_route_us_v1_ssa_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all special security areas traversed by route.

    Retrieve all special security areas intersected by route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = SSAByRoute.from_dict(body)
    return web.Response(status=200)
