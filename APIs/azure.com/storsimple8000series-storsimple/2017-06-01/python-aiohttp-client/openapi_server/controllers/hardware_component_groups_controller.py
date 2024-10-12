from typing import List, Dict
from aiohttp import web

from openapi_server.models.controller_power_state_change_request import ControllerPowerStateChangeRequest
from openapi_server.models.hardware_component_group_list import HardwareComponentGroupList
from openapi_server import util


async def hardware_component_groups_change_controller_power_state(request: web.Request, device_name, hardware_component_group_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """hardware_component_groups_change_controller_power_state

    Changes the power state of the controller.

    :param device_name: The device name
    :type device_name: str
    :param hardware_component_group_name: The hardware component group name.
    :type hardware_component_group_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The controller power state change request.
    :type parameters: dict | bytes

    """
    parameters = ControllerPowerStateChangeRequest.from_dict(parameters)
    return web.Response(status=200)


async def hardware_component_groups_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """hardware_component_groups_list_by_device

    Lists the hardware component groups at device-level.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)
