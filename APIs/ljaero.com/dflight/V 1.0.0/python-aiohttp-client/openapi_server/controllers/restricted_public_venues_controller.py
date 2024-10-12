from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.venue_distance_response import VenueDistanceResponse
from openapi_server.models.venue_poly_response import VenuePolyResponse
from openapi_server.models.venue_route_response import VenueRouteResponse
from openapi_server.models.venues_by_distance import VenuesByDistance
from openapi_server.models.venues_by_polygon import VenuesByPolygon
from openapi_server.models.venues_by_route import VenuesByRoute
from openapi_server import util


async def ven_by_distance_us_v1_venues_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all restricted public venues located within given distance of location.

    Retrieve venues existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000)

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = VenuesByDistance.from_dict(body)
    return web.Response(status=200)


async def ven_by_poly_us_v1_venues_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all restricted public venues located within given GeoJSON Polygon.

    Retrieve all restricted public venues located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = VenuesByPolygon.from_dict(body)
    return web.Response(status=200)


async def ven_by_route_us_v1_venues_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all restricted public venues traversed by route.

    Retrieve all restricted public venues intersected by route. Request body parameters are: * route: [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km.

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = VenuesByRoute.from_dict(body)
    return web.Response(status=200)
