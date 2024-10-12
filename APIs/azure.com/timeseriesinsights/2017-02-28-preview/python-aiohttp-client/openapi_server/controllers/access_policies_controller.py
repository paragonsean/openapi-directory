from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_policy_create_or_update_parameters import AccessPolicyCreateOrUpdateParameters
from openapi_server.models.access_policy_list_response import AccessPolicyListResponse
from openapi_server.models.access_policy_resource import AccessPolicyResource
from openapi_server.models.access_policy_update_parameters import AccessPolicyUpdateParameters
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def access_policies_create_or_update(request: web.Request, subscription_id, resource_group_name, environment_name, access_policy_name, api_version, parameters) -> web.Response:
    """access_policies_create_or_update

    Create or update an access policy in the specified environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param access_policy_name: Name of the access policy.
    :type access_policy_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str
    :param parameters: Parameters for creating an access policy.
    :type parameters: dict | bytes

    """
    parameters = AccessPolicyCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def access_policies_delete(request: web.Request, subscription_id, resource_group_name, environment_name, access_policy_name, api_version) -> web.Response:
    """access_policies_delete

    Deletes the access policy with the specified name in the specified subscription, resource group, and environment

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param access_policy_name: The name of the Time Series Insights access policy associated with the specified environment.
    :type access_policy_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def access_policies_get(request: web.Request, subscription_id, resource_group_name, environment_name, access_policy_name, api_version) -> web.Response:
    """access_policies_get

    Gets the access policy with the specified name in the specified environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param access_policy_name: The name of the Time Series Insights access policy associated with the specified environment.
    :type access_policy_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def access_policies_list_by_environment(request: web.Request, subscription_id, resource_group_name, environment_name, api_version) -> web.Response:
    """access_policies_list_by_environment

    Lists all the available access policies associated with the environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def access_policies_update(request: web.Request, subscription_id, resource_group_name, environment_name, access_policy_name, api_version, access_policy_update_parameters) -> web.Response:
    """access_policies_update

    Updates the access policy with the specified name in the specified subscription, resource group, and environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param access_policy_name: The name of the Time Series Insights access policy associated with the specified environment.
    :type access_policy_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str
    :param access_policy_update_parameters: Request object that contains the updated information for the access policy.
    :type access_policy_update_parameters: dict | bytes

    """
    access_policy_update_parameters = AccessPolicyUpdateParameters.from_dict(access_policy_update_parameters)
    return web.Response(status=200)
