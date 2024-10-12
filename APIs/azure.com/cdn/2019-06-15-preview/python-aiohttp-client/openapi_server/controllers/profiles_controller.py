from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.profile import Profile
from openapi_server.models.profile_list_result import ProfileListResult
from openapi_server.models.profile_update_parameters import ProfileUpdateParameters
from openapi_server.models.resource_usage_list_result import ResourceUsageListResult
from openapi_server.models.sso_uri import SsoUri
from openapi_server.models.supported_optimization_types_list_result import SupportedOptimizationTypesListResult
from openapi_server import util


async def profiles_create(request: web.Request, resource_group_name, profile_name, subscription_id, api_version, profile) -> web.Response:
    """profiles_create

    Creates a new CDN profile with a profile name under the specified subscription and resource group.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param profile: Profile properties needed to create a new profile.
    :type profile: dict | bytes

    """
    profile = Profile.from_dict(profile)
    return web.Response(status=200)


async def profiles_delete(request: web.Request, resource_group_name, profile_name, subscription_id, api_version) -> web.Response:
    """profiles_delete

    Deletes an existing CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def profiles_generate_sso_uri(request: web.Request, resource_group_name, profile_name, subscription_id, api_version) -> web.Response:
    """profiles_generate_sso_uri

    Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def profiles_get(request: web.Request, resource_group_name, profile_name, subscription_id, api_version) -> web.Response:
    """profiles_get

    Gets a CDN profile with the specified profile name under the specified subscription and resource group.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def profiles_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """profiles_list

    Lists all of the CDN profiles within an Azure subscription.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def profiles_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """profiles_list_by_resource_group

    Lists all of the CDN profiles within a resource group.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def profiles_list_resource_usage(request: web.Request, resource_group_name, profile_name, subscription_id, api_version) -> web.Response:
    """profiles_list_resource_usage

    Checks the quota and actual usage of endpoints under the given CDN profile.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def profiles_list_supported_optimization_types(request: web.Request, resource_group_name, profile_name, subscription_id, api_version) -> web.Response:
    """profiles_list_supported_optimization_types

    Gets the supported optimization types for the current profile. A user can create an endpoint with an optimization type from the listed values.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def profiles_update(request: web.Request, resource_group_name, profile_name, subscription_id, api_version, profile_update_parameters) -> web.Response:
    """profiles_update

    Updates an existing CDN profile with the specified profile name under the specified subscription and resource group.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param profile_update_parameters: Profile properties needed to update an existing profile.
    :type profile_update_parameters: dict | bytes

    """
    profile_update_parameters = ProfileUpdateParameters.from_dict(profile_update_parameters)
    return web.Response(status=200)
