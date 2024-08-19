from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_set import AvailabilitySet
from openapi_server.models.availability_set_list_result import AvailabilitySetListResult
from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.resource_skus_result import ResourceSkusResult
from openapi_server.models.virtual_machine_size_list_result import VirtualMachineSizeListResult
from openapi_server import util


async def availability_sets_create_or_update(request: web.Request, resource_group_name, availability_set_name, api_version, subscription_id, parameters) -> web.Response:
    """availability_sets_create_or_update

    Create or update an availability set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param availability_set_name: The name of the availability set.
    :type availability_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Availability Set operation.
    :type parameters: dict | bytes

    """
    parameters = AvailabilitySet.from_dict(parameters)
    return web.Response(status=200)


async def availability_sets_delete(request: web.Request, resource_group_name, availability_set_name, api_version, subscription_id) -> web.Response:
    """availability_sets_delete

    Delete an availability set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param availability_set_name: The name of the availability set.
    :type availability_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def availability_sets_get(request: web.Request, resource_group_name, availability_set_name, api_version, subscription_id) -> web.Response:
    """availability_sets_get

    Retrieves information about an availability set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param availability_set_name: The name of the availability set.
    :type availability_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def availability_sets_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """availability_sets_list

    Lists all availability sets in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def availability_sets_list_available_sizes(request: web.Request, resource_group_name, availability_set_name, api_version, subscription_id) -> web.Response:
    """availability_sets_list_available_sizes

    Lists all available virtual machine sizes that can be used to create a new virtual machine in an existing availability set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param availability_set_name: The name of the availability set.
    :type availability_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def availability_sets_list_by_subscription(request: web.Request, api_version, subscription_id, expand=None) -> web.Response:
    """availability_sets_list_by_subscription

    Lists all availability sets in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The expand expression to apply to the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def resource_skus_list_0(request: web.Request, api_version, subscription_id) -> web.Response:
    """resource_skus_list_0

    Gets the list of Microsoft.Compute SKUs available for your Subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
