from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_floor_plan_request import CreateNetworkFloorPlanRequest
from openapi_server.models.update_network_floor_plan_request import UpdateNetworkFloorPlanRequest
from openapi_server import util


async def create_network_floor_plan_1(request: web.Request, network_id, body) -> web.Response:
    """Upload a floor plan

    Upload a floor plan

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFloorPlanRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_floor_plan_1(request: web.Request, network_id, floor_plan_id) -> web.Response:
    """Destroy a floor plan

    Destroy a floor plan

    :param network_id: 
    :type network_id: str
    :param floor_plan_id: 
    :type floor_plan_id: str

    """
    return web.Response(status=200)


async def get_network_floor_plan_1(request: web.Request, network_id, floor_plan_id) -> web.Response:
    """Find a floor plan by ID

    Find a floor plan by ID

    :param network_id: 
    :type network_id: str
    :param floor_plan_id: 
    :type floor_plan_id: str

    """
    return web.Response(status=200)


async def get_network_floor_plans_1(request: web.Request, network_id) -> web.Response:
    """List the floor plans that belong to your network

    List the floor plans that belong to your network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_floor_plan_1(request: web.Request, network_id, floor_plan_id, body=None) -> web.Response:
    """Update a floor plan&#39;s geolocation and other meta data

    Update a floor plan&#39;s geolocation and other meta data

    :param network_id: 
    :type network_id: str
    :param floor_plan_id: 
    :type floor_plan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFloorPlanRequest.from_dict(body)
    return web.Response(status=200)
