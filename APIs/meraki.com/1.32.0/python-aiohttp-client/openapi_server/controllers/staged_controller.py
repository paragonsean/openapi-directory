from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_staged_event_request import CreateNetworkFirmwareUpgradesStagedEventRequest
from openapi_server.models.create_network_firmware_upgrades_staged_group_request import CreateNetworkFirmwareUpgradesStagedGroupRequest
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response import GetNetworkFirmwareUpgradesStagedEvents200Response
from openapi_server.models.get_network_firmware_upgrades_staged_groups200_response_inner import GetNetworkFirmwareUpgradesStagedGroups200ResponseInner
from openapi_server.models.get_network_firmware_upgrades_staged_stages200_response_inner import GetNetworkFirmwareUpgradesStagedStages200ResponseInner
from openapi_server.models.rollbacks_network_firmware_upgrades_staged_events_request import RollbacksNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_events_request import UpdateNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_stages_request import UpdateNetworkFirmwareUpgradesStagedStagesRequest
from openapi_server import util


async def create_network_firmware_upgrades_staged_event_2(request: web.Request, network_id, body) -> web.Response:
    """Create a Staged Upgrade Event for a network

    Create a Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedEventRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_firmware_upgrades_staged_group_2(request: web.Request, network_id, body) -> web.Response:
    """Create a Staged Upgrade Group for a network

    Create a Staged Upgrade Group for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedGroupRequest.from_dict(body)
    return web.Response(status=200)


async def defer_network_firmware_upgrades_staged_events_2(request: web.Request, network_id) -> web.Response:
    """Postpone by 1 week all pending staged upgrade stages for a network

    Postpone by 1 week all pending staged upgrade stages for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def delete_network_firmware_upgrades_staged_group_2(request: web.Request, network_id, group_id) -> web.Response:
    """Delete a Staged Upgrade Group

    Delete a Staged Upgrade Group

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_events_2(request: web.Request, network_id) -> web.Response:
    """Get the Staged Upgrade Event from a network

    Get the Staged Upgrade Event from a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_group_2(request: web.Request, network_id, group_id) -> web.Response:
    """Get a Staged Upgrade Group from a network

    Get a Staged Upgrade Group from a network

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_groups_2(request: web.Request, network_id) -> web.Response:
    """List of Staged Upgrade Groups in a network

    List of Staged Upgrade Groups in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_stages_2(request: web.Request, network_id) -> web.Response:
    """Order of Staged Upgrade Groups in a network

    Order of Staged Upgrade Groups in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def rollbacks_network_firmware_upgrades_staged_events_2(request: web.Request, network_id, body) -> web.Response:
    """Rollback a Staged Upgrade Event for a network

    Rollback a Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RollbacksNetworkFirmwareUpgradesStagedEventsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_events_2(request: web.Request, network_id, body) -> web.Response:
    """Update the Staged Upgrade Event for a network

    Update the Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFirmwareUpgradesStagedEventsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_group_2(request: web.Request, network_id, group_id, body) -> web.Response:
    """Update a Staged Upgrade Group for a network

    Update a Staged Upgrade Group for a network

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_stages_2(request: web.Request, network_id, body=None) -> web.Response:
    """Assign Staged Upgrade Group order in the sequence.

    Assign Staged Upgrade Group order in the sequence.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFirmwareUpgradesStagedStagesRequest.from_dict(body)
    return web.Response(status=200)
