from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_stop_response import V3StopResponse
from openapi_server.models.v3_stops_by_distance_response import V3StopsByDistanceResponse
from openapi_server.models.v3_stops_on_route_response import V3StopsOnRouteResponse
from openapi_server import util


async def stops_stop_details(request: web.Request, stop_id, route_type, stop_location=None, stop_amenities=None, stop_accessibility=None, stop_contact=None, stop_ticket=None, gtfs=None, stop_staffing=None, stop_disruptions=None, token=None, devid=None, signature=None) -> web.Response:
    """View facilities at a specific stop (Metro and V/Line stations only)

    

    :param stop_id: Identifier of stop; values returned by Stops API
    :type stop_id: int
    :param route_type: Number identifying transport mode; values returned via RouteTypes API
    :type route_type: int
    :param stop_location: Indicates if stop location information will be returned (default &#x3D; false)
    :type stop_location: bool
    :param stop_amenities: Indicates if stop amenity information will be returned (default &#x3D; false)
    :type stop_amenities: bool
    :param stop_accessibility: Indicates if stop accessibility information will be returned (default &#x3D; false)
    :type stop_accessibility: bool
    :param stop_contact: Indicates if stop contact information will be returned (default &#x3D; false)
    :type stop_contact: bool
    :param stop_ticket: Indicates if stop ticket information will be returned (default &#x3D; false)
    :type stop_ticket: bool
    :param gtfs: Incdicates whether the stop_id is a GTFS ID or not
    :type gtfs: bool
    :param stop_staffing: Indicates if stop staffing information will be returned (default &#x3D; false)
    :type stop_staffing: bool
    :param stop_disruptions: Indicates if stop disruption information will be returned (default &#x3D; false)
    :type stop_disruptions: bool
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def stops_stops_by_geolocation(request: web.Request, latitude, longitude, route_types=None, max_results=None, max_distance=None, stop_disruptions=None, token=None, devid=None, signature=None) -> web.Response:
    """View all stops near a specific location

    

    :param latitude: Geographic coordinate of latitude
    :type latitude: float
    :param longitude: Geographic coordinate of longitude
    :type longitude: float
    :param route_types: Filter by route_type; values returned via RouteTypes API
    :type route_types: List[int]
    :param max_results: Maximum number of results returned (default &#x3D; 30)
    :type max_results: int
    :param max_distance: Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default &#x3D; 300)
    :type max_distance: float
    :param stop_disruptions: Indicates if stop disruption information will be returned (default &#x3D; false)
    :type stop_disruptions: bool
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def stops_stops_for_route(request: web.Request, route_id, route_type, direction_id=None, stop_disruptions=None, include_geopath=None, geopath_utc=None, token=None, devid=None, signature=None) -> web.Response:
    """View all stops on a specific route

    

    :param route_id: Identifier of route; values returned by Routes API - v3/routes
    :type route_id: int
    :param route_type: Number identifying transport mode; values returned via RouteTypes API
    :type route_type: int
    :param direction_id: An optional direction; values returned by Directions API. When this is set, stop sequence information is returned in the response.
    :type direction_id: int
    :param stop_disruptions: Indicates if stop disruption information will be returned (default &#x3D; false)
    :type stop_disruptions: bool
    :param include_geopath: Indicates if geopath data will be returned (default &#x3D; false)
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
