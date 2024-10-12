from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_run_response import V3RunResponse
from openapi_server.models.v3_runs_response import V3RunsResponse
from openapi_server import util


async def runs_for_route(request: web.Request, route_id, expand=None, date_utc=None, token=None, devid=None, signature=None) -> web.Response:
    """View all trip/service runs for a specific route ID

    

    :param route_id: Identifier of route; values returned by Routes API - v3/routes.
    :type route_id: int
    :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None.
    :type expand: List[str]
    :param date_utc: Date of the request. (optional - defaults to now)
    :type date_utc: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    date_utc = util.deserialize_datetime(date_utc)
    return web.Response(status=200)


async def runs_for_route_and_route_type(request: web.Request, route_id, route_type, expand, date_utc=None, token=None, devid=None, signature=None) -> web.Response:
    """View all trip/service runs for a specific route ID and route type

    

    :param route_id: Identifier of route; values returned by Routes API - v3/routes.
    :type route_id: int
    :param route_type: Number identifying transport mode; values returned via RouteTypes API
    :type route_type: int
    :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is All.
    :type expand: List[str]
    :param date_utc: Date of the request. (optional - defaults to now)
    :type date_utc: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    date_utc = util.deserialize_datetime(date_utc)
    return web.Response(status=200)


async def runs_for_run(request: web.Request, run_ref, expand, date_utc=None, include_geopath=None, token=None, devid=None, signature=None) -> web.Response:
    """View all trip/service runs for a specific run_ref

    

    :param run_ref: The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead.
    :type run_ref: str
    :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None.
    :type expand: List[str]
    :param date_utc: Date of the request. (optional - defaults to now)
    :type date_utc: str
    :param include_geopath: Indicates if geopath data will be returned (default &#x3D; false)
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


async def runs_for_run_and_route_type(request: web.Request, run_ref, route_type, expand, date_utc=None, include_geopath=None, token=None, devid=None, signature=None) -> web.Response:
    """View the trip/service run for a specific run_ref and route type

    

    :param run_ref: The run_ref is the identifier of a run as returned by the departures/* and runs/* endpoints. WARNING, run_id is deprecated. Use run_ref instead.
    :type run_ref: str
    :param route_type: Number identifying transport mode; values returned via RouteTypes API
    :type route_type: int
    :param expand: List of objects to be returned in full (i.e. expanded) - options include: All, VehiclePosition, VehicleDescriptor, or None. Default is None.
    :type expand: List[str]
    :param date_utc: Date of the request. (optional - defaults to now)
    :type date_utc: str
    :param include_geopath: Indicates if geopath data will be returned (default &#x3D; false)
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
