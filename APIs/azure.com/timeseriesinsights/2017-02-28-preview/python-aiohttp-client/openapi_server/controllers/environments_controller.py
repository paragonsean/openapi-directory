from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment_create_or_update_parameters import EnvironmentCreateOrUpdateParameters
from openapi_server.models.environment_list_response import EnvironmentListResponse
from openapi_server.models.environment_resource import EnvironmentResource
from openapi_server.models.environment_update_parameters import EnvironmentUpdateParameters
from openapi_server import util


async def environments_create_or_update(request: web.Request, subscription_id, resource_group_name, environment_name, api_version, parameters) -> web.Response:
    """environments_create_or_update

    Create or update an environment in the specified subscription and resource group.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: Name of the environment
    :type environment_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str
    :param parameters: Parameters for creating an environment resource.
    :type parameters: dict | bytes

    """
    parameters = EnvironmentCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def environments_delete(request: web.Request, subscription_id, resource_group_name, environment_name, api_version) -> web.Response:
    """environments_delete

    Deletes the environment with the specified name in the specified subscription and resource group.

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


async def environments_get(request: web.Request, subscription_id, resource_group_name, environment_name, api_version) -> web.Response:
    """environments_get

    Gets the environment with the specified name in the specified subscription and resource group.

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


async def environments_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """environments_list_by_resource_group

    Lists all the available environments associated with the subscription and within the specified resource group.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def environments_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """environments_list_by_subscription

    Lists all the available environments within a subscription, irrespective of the resource groups.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def environments_update(request: web.Request, subscription_id, resource_group_name, environment_name, api_version, environment_update_parameters) -> web.Response:
    """environments_update

    Updates the environment with the specified name in the specified subscription and resource group.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str
    :param environment_update_parameters: Request object that contains the updated information for the environment.
    :type environment_update_parameters: dict | bytes

    """
    environment_update_parameters = EnvironmentUpdateParameters.from_dict(environment_update_parameters)
    return web.Response(status=200)
