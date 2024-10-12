from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.name_availability import NameAvailability
from openapi_server.models.name_availability_parameters import NameAvailabilityParameters
from openapi_server.models.operation_list import OperationList
from openapi_server.models.regenerate_key_parameters import RegenerateKeyParameters
from openapi_server.models.signal_r_create_parameters import SignalRCreateParameters
from openapi_server.models.signal_r_keys import SignalRKeys
from openapi_server.models.signal_r_resource import SignalRResource
from openapi_server.models.signal_r_resource_list import SignalRResourceList
from openapi_server.models.signal_r_update_parameters import SignalRUpdateParameters
from openapi_server.models.signal_r_usage_list import SignalRUsageList
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available REST API operations of the Microsoft.SignalRService provider.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def signal_r_check_name_availability(request: web.Request, location, api_version, subscription_id, parameters=None) -> web.Response:
    """signal_r_check_name_availability

    Checks that the SignalR name is valid and is not already in use.

    :param location: the region
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = NameAvailabilityParameters.from_dict(parameters)
    return web.Response(status=200)


async def signal_r_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters=None) -> web.Response:
    """signal_r_create_or_update

    Create a new SignalR service and update an exiting SignalR service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param resource_name: The name of the SignalR resource.
    :type resource_name: str
    :param parameters: Parameters for the create or update operation
    :type parameters: dict | bytes

    """
    parameters = SignalRCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def signal_r_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """signal_r_delete

    Operation to delete a SignalR service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param resource_name: The name of the SignalR resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def signal_r_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """signal_r_get

    Get the SignalR service and its properties.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param resource_name: The name of the SignalR resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def signal_r_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """signal_r_list_by_resource_group

    Handles requests to list all resources in a resource group.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def signal_r_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """signal_r_list_by_subscription

    Handles requests to list all resources in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def signal_r_list_keys(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """signal_r_list_keys

    Get the access keys of the SignalR resource.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param resource_name: The name of the SignalR resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def signal_r_regenerate_key(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters=None) -> web.Response:
    """signal_r_regenerate_key

    Regenerate SignalR service access key. PrimaryKey and SecondaryKey cannot be regenerated at the same time.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param resource_name: The name of the SignalR resource.
    :type resource_name: str
    :param parameters: Parameter that describes the Regenerate Key Operation.
    :type parameters: dict | bytes

    """
    parameters = RegenerateKeyParameters.from_dict(parameters)
    return web.Response(status=200)


async def signal_r_restart(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """signal_r_restart

    Operation to restart a SignalR service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param resource_name: The name of the SignalR resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def signal_r_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, parameters=None) -> web.Response:
    """signal_r_update

    Operation to update an exiting SignalR service.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param resource_name: The name of the SignalR resource.
    :type resource_name: str
    :param parameters: Parameters for the update operation
    :type parameters: dict | bytes

    """
    parameters = SignalRUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def usages_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """usages_list

    List usage quotas for Azure SignalR service by location.

    :param location: the location like \&quot;eastus\&quot;
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
