from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.uoas_by_distance import UOAsByDistance
from openapi_server.models.uoas_by_polygon import UOAsByPolygon
from openapi_server.models.uoas_by_route import UOAsByRoute
from openapi_server.models.uoas_distance_response import UOAsDistanceResponse
from openapi_server.models.uoas_poly_response import UOAsPolyResponse
from openapi_server.models.uoas_route_response import UOAsRouteResponse
from openapi_server import util


async def uoa_by_distance_us_v1_uoa_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve UAS Operating Areas (UOAs) found within given distance of location.

    Retrieve UAS Operating Areas (UOAs) found within given distance of a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = UOAsByDistance.from_dict(body)
    return web.Response(status=200)


async def uoa_by_poly_us_v1_uoa_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve UAS Operating Areas (UOAs) found within given area.

    Retrieve UAS Operating Areas (UOAs) found within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = UOAsByPolygon.from_dict(body)
    return web.Response(status=200)


async def uoa_by_route_us_v1_uoa_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve UAS Operating Areas (UOAs) found along route.

    Retrieve UAS Operating Areas (UOAs) found along your route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = UOAsByRoute.from_dict(body)
    return web.Response(status=200)
