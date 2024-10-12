from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_disruption_modes_response import V3DisruptionModesResponse
from openapi_server.models.v3_disruption_response import V3DisruptionResponse
from openapi_server.models.v3_disruptions_response import V3DisruptionsResponse
from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server import util


async def disruptions_get_all_disruptions(request: web.Request, route_types=None, disruption_modes=None, disruption_status=None, token=None, devid=None, signature=None) -> web.Response:
    """View all disruptions for all route types

    

    :param route_types: Filter by route_type; values returned via RouteTypes API
    :type route_types: List[int]
    :param disruption_modes: Filter by disruption_mode; values returned via v3/disruptions/modes API
    :type disruption_modes: List[int]
    :param disruption_status: Filter by status of disruption
    :type disruption_status: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def disruptions_get_disruption_by_id(request: web.Request, disruption_id, token=None, devid=None, signature=None) -> web.Response:
    """View a specific disruption

    

    :param disruption_id: Identifier of disruption; values returned by Disruptions API - /v3/disruptions OR /v3/disruptions/route/{route_id}
    :type disruption_id: int
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def disruptions_get_disruption_modes(request: web.Request, token=None, devid=None, signature=None) -> web.Response:
    """Get all disruption modes

    

    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def disruptions_get_disruptions_by_route(request: web.Request, route_id, disruption_status=None, token=None, devid=None, signature=None) -> web.Response:
    """View all disruptions for a particular route

    

    :param route_id: Identifier of route; values returned by Routes API - v3/routes
    :type route_id: int
    :param disruption_status: Filter by status of disruption
    :type disruption_status: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def disruptions_get_disruptions_by_route_and_stop(request: web.Request, route_id, stop_id, disruption_status=None, token=None, devid=None, signature=None) -> web.Response:
    """View all disruptions for a particular route and stop

    

    :param route_id: Identifier of route; values returned by Routes API - v3/routes
    :type route_id: int
    :param stop_id: Identifier of stop; values returned by Stops API - v3/stops
    :type stop_id: int
    :param disruption_status: Filter by status of disruption
    :type disruption_status: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)


async def disruptions_get_disruptions_by_stop(request: web.Request, stop_id, disruption_status=None, token=None, devid=None, signature=None) -> web.Response:
    """View all disruptions for a particular stop

    

    :param stop_id: Identifier of stop; values returned by Stops API - v3/stops
    :type stop_id: int
    :param disruption_status: Filter by status of disruption
    :type disruption_status: str
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)
