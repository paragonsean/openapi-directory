from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_traffic_manager_relative_dns_name_availability_parameters import CheckTrafficManagerRelativeDnsNameAvailabilityParameters
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.delete_operation_result import DeleteOperationResult
from openapi_server.models.profile import Profile
from openapi_server.models.profile_list_result import ProfileListResult
from openapi_server.models.traffic_manager_name_availability import TrafficManagerNameAvailability
from openapi_server import util


async def profiles_check_traffic_manager_relative_dns_name_availability(request: web.Request, api_version, parameters) -> web.Response:
    """profiles_check_traffic_manager_relative_dns_name_availability

    Checks the availability of a Traffic Manager Relative DNS name.

    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The Traffic Manager name parameters supplied to the CheckTrafficManagerNameAvailability operation.
    :type parameters: dict | bytes

    """
    parameters = CheckTrafficManagerRelativeDnsNameAvailabilityParameters.from_dict(parameters)
    return web.Response(status=200)


async def profiles_create_or_update(request: web.Request, resource_group_name, profile_name, api_version, subscription_id, parameters) -> web.Response:
    """profiles_create_or_update

    Create or update a Traffic Manager profile.

    :param resource_group_name: The name of the resource group containing the Traffic Manager profile.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The Traffic Manager profile parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = Profile.from_dict(parameters)
    return web.Response(status=200)


async def profiles_delete(request: web.Request, resource_group_name, profile_name, api_version, subscription_id) -> web.Response:
    """profiles_delete

    Deletes a Traffic Manager profile.

    :param resource_group_name: The name of the resource group containing the Traffic Manager profile to be deleted.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile to be deleted.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def profiles_get(request: web.Request, resource_group_name, profile_name, api_version, subscription_id) -> web.Response:
    """profiles_get

    Gets a Traffic Manager profile.

    :param resource_group_name: The name of the resource group containing the Traffic Manager profile.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def profiles_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """profiles_list_all

    Lists all Traffic Manager profiles within a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def profiles_list_all_in_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """profiles_list_all_in_resource_group

    Lists all Traffic Manager profiles within a resource group.

    :param resource_group_name: The name of the resource group containing the Traffic Manager profiles to be listed.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def profiles_update(request: web.Request, resource_group_name, profile_name, api_version, subscription_id, parameters) -> web.Response:
    """profiles_update

    Update a Traffic Manager profile.

    :param resource_group_name: The name of the resource group containing the Traffic Manager profile.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The Traffic Manager profile parameters supplied to the Update operation.
    :type parameters: dict | bytes

    """
    parameters = Profile.from_dict(parameters)
    return web.Response(status=200)
