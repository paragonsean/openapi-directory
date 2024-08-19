from typing import List, Dict
from aiohttp import web

from openapi_server.models.proximity_placement_group import ProximityPlacementGroup
from openapi_server.models.proximity_placement_group_list_result import ProximityPlacementGroupListResult
from openapi_server.models.proximity_placement_group_update import ProximityPlacementGroupUpdate
from openapi_server import util


async def proximity_placement_groups_create_or_update(request: web.Request, resource_group_name, proximity_placement_group_name, api_version, subscription_id, parameters) -> web.Response:
    """proximity_placement_groups_create_or_update

    Create or update a proximity placement group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param proximity_placement_group_name: The name of the proximity placement group.
    :type proximity_placement_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Proximity Placement Group operation.
    :type parameters: dict | bytes

    """
    parameters = ProximityPlacementGroup.from_dict(parameters)
    return web.Response(status=200)


async def proximity_placement_groups_delete(request: web.Request, resource_group_name, proximity_placement_group_name, api_version, subscription_id) -> web.Response:
    """proximity_placement_groups_delete

    Delete a proximity placement group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param proximity_placement_group_name: The name of the proximity placement group.
    :type proximity_placement_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def proximity_placement_groups_get(request: web.Request, resource_group_name, proximity_placement_group_name, api_version, subscription_id) -> web.Response:
    """proximity_placement_groups_get

    Retrieves information about a proximity placement group .

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param proximity_placement_group_name: The name of the proximity placement group.
    :type proximity_placement_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def proximity_placement_groups_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """proximity_placement_groups_list_by_resource_group

    Lists all proximity placement groups in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def proximity_placement_groups_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """proximity_placement_groups_list_by_subscription

    Lists all proximity placement groups in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def proximity_placement_groups_update(request: web.Request, resource_group_name, proximity_placement_group_name, api_version, subscription_id, parameters) -> web.Response:
    """proximity_placement_groups_update

    Update a proximity placement group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param proximity_placement_group_name: The name of the proximity placement group.
    :type proximity_placement_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update Proximity Placement Group operation.
    :type parameters: dict | bytes

    """
    parameters = ProximityPlacementGroupUpdate.from_dict(parameters)
    return web.Response(status=200)
