from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_route_response import V3RouteResponse
from openapi_server import util


async def routes_one_or_more_routes(request: web.Request, route_types=None, route_name=None, token=None, devid=None, signature=None) -> web.Response:
    """View route names and numbers for all routes

    

    :param route_types: Filter by route_type; values returned via RouteTypes API
    :type route_types: List[int]
    :param route_name: Filter by name  of route (accepts partial route name matches)
    :type route_name: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def routes_route_from_id(request: web.Request, route_id, include_geopath=None, geopath_utc=None, token=None, devid=None, signature=None) -> web.Response:
    """View route name and number for specific route ID

    

    :param route_id: Identifier of route; values returned by Departures, Directions and Disruptions APIs
    :type route_id: int
    :param include_geopath: Indicates kif geopath data will be returned (default &#x3D; false)
    :type include_geopath: bool
    :param geopath_utc: Filter geopaths by date (ISO 8601 UTC format) (default &#x3D; current date)
    :type geopath_utc: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    geopath_utc = util.deserialize_datetime(geopath_utc)
    return web.Response(status=200)
