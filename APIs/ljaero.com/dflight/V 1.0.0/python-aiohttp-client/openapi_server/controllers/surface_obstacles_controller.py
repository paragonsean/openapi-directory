from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.obstacle_distance_response import ObstacleDistanceResponse
from openapi_server.models.obstacle_poly_response import ObstaclePolyResponse
from openapi_server.models.obstacle_route_response import ObstacleRouteResponse
from openapi_server.models.obstacles_by_distance import ObstaclesByDistance
from openapi_server.models.obstacles_by_polygon import ObstaclesByPolygon
from openapi_server.models.obstacles_by_route import ObstaclesByRoute
from openapi_server import util


async def obstacles_by_distance_us_v1_obstacles_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve obstacles within given distance of location.

    Retrieve obstacles within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = ObstaclesByDistance.from_dict(body)
    return web.Response(status=200)


async def obstacles_by_poly_us_v1_obstacles_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve obstacles located within given area.

    Retrieve obstacles located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = ObstaclesByPolygon.from_dict(body)
    return web.Response(status=200)


async def obstacles_by_route_us_v1_obstacles_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve obstacles found along a route.

    Retrieve obstacles found along a route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = ObstaclesByRoute.from_dict(body)
    return web.Response(status=200)
