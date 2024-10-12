from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_departures_response import V3DeparturesResponse
from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server import util


async def departures_get_for_stop(request: web.Request, route_type, stop_id, platform_numbers=None, direction_id=None, gtfs=None, date_utc=None, max_results=None, include_cancelled=None, look_backwards=None, expand=None, include_geopath=None, token=None, devid=None, signature=None) -> web.Response:
    """View departures for all routes from a stop

    

    :param route_type: Number identifying transport mode; values returned via RouteTypes API
    :type route_type: int
    :param stop_id: Identifier of stop; values returned by Stops API
    :type stop_id: int
    :param platform_numbers: Filter by platform number at stop
    :type platform_numbers: List[int]
    :param direction_id: Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    :type direction_id: int
    :param gtfs: Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data
    :type gtfs: bool
    :param date_utc: Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time)
    :type date_utc: str
    :param max_results: Maximum number of results returned
    :type max_results: int
    :param include_cancelled: Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only
    :type include_cancelled: bool
    :param look_backwards: Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0.
    :type look_backwards: bool
    :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    :type expand: List[str]
    :param include_geopath: Indicates if the route geopath should be returned
    :type include_geopath: bool
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    date_utc = util.deserialize_datetime(date_utc)
    return web.Response(status=200)


async def departures_get_for_stop_and_route(request: web.Request, route_type, stop_id, route_id, direction_id=None, gtfs=None, date_utc=None, max_results=None, include_cancelled=None, look_backwards=None, expand=None, include_geopath=None, token=None, devid=None, signature=None) -> web.Response:
    """View departures for a specific route from a stop

    

    :param route_type: Number identifying transport mode; values returned via RouteTypes API
    :type route_type: int
    :param stop_id: Identifier of stop; values returned by Stops API
    :type stop_id: int
    :param route_id: Identifier of route; values returned by Routes API - v3/routes
    :type route_id: str
    :param direction_id: Filter by identifier of direction of travel; values returned by Directions API - /v3/directions/route/{route_id}
    :type direction_id: int
    :param gtfs: Indicates that stop_id parameter will accept \&quot;GTFS stop_id\&quot; data
    :type gtfs: bool
    :param date_utc: Filter by the date and time of the request (ISO 8601 UTC format) (default &#x3D; current date and time)
    :type date_utc: str
    :param max_results: Maximum number of results returned
    :type max_results: int
    :param include_cancelled: Indicates if cancelled services (if they exist) are returned (default &#x3D; false) - metropolitan train only
    :type include_cancelled: bool
    :param look_backwards: Indicates if filtering runs (and their departures) to those that arrive at destination before date_utc (default &#x3D; false). Requires max_results &amp;gt; 0.
    :type look_backwards: bool
    :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, Stop, Route, Run, Direction, Disruption, VehiclePosition, VehicleDescriptor or None.              Run must be expanded to receive VehiclePosition and VehicleDescriptor information.
    :type expand: List[str]
    :param include_geopath: Indicates if the route geopath should be returned
    :type include_geopath: bool
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    date_utc = util.deserialize_datetime(date_utc)
    return web.Response(status=200)
