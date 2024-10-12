from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_switch_port_schedule_request import CreateNetworkSwitchPortScheduleRequest
from openapi_server.models.update_network_switch_port_schedule_request import UpdateNetworkSwitchPortScheduleRequest
from openapi_server import util


async def create_network_switch_port_schedule(request: web.Request, network_id, body) -> web.Response:
    """Add a switch port schedule

    Add a switch port schedule

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchPortScheduleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_port_schedule(request: web.Request, network_id, port_schedule_id) -> web.Response:
    """Delete a switch port schedule

    Delete a switch port schedule

    :param network_id: 
    :type network_id: str
    :param port_schedule_id: 
    :type port_schedule_id: str

    """
    return web.Response(status=200)


async def get_network_switch_port_schedules(request: web.Request, network_id) -> web.Response:
    """List switch port schedules

    List switch port schedules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_port_schedule(request: web.Request, network_id, port_schedule_id, body=None) -> web.Response:
    """Update a switch port schedule

    Update a switch port schedule

    :param network_id: 
    :type network_id: str
    :param port_schedule_id: 
    :type port_schedule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchPortScheduleRequest.from_dict(body)
    return web.Response(status=200)
