from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.event_source_create_or_update_parameters import EventSourceCreateOrUpdateParameters
from openapi_server.models.event_source_list_response import EventSourceListResponse
from openapi_server.models.event_source_resource import EventSourceResource
from openapi_server.models.event_source_update_parameters import EventSourceUpdateParameters
from openapi_server import util


async def event_sources_create_or_update(request: web.Request, subscription_id, resource_group_name, environment_name, event_source_name, api_version, parameters) -> web.Response:
    """event_sources_create_or_update

    Create or update an event source under the specified environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param event_source_name: Name of the event source.
    :type event_source_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str
    :param parameters: Parameters for creating an event source resource.
    :type parameters: dict | bytes

    """
    parameters = EventSourceCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def event_sources_delete(request: web.Request, subscription_id, resource_group_name, environment_name, event_source_name, api_version) -> web.Response:
    """event_sources_delete

    Deletes the event source with the specified name in the specified subscription, resource group, and environment

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :type event_source_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_sources_get(request: web.Request, subscription_id, resource_group_name, environment_name, event_source_name, api_version) -> web.Response:
    """event_sources_get

    Gets the event source with the specified name in the specified environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :type event_source_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_sources_list_by_environment(request: web.Request, subscription_id, resource_group_name, environment_name, api_version) -> web.Response:
    """event_sources_list_by_environment

    Lists all the available event sources associated with the subscription and within the specified resource group and environment.

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


async def event_sources_update(request: web.Request, subscription_id, resource_group_name, environment_name, event_source_name, api_version, event_source_update_parameters) -> web.Response:
    """event_sources_update

    Updates the event source with the specified name in the specified subscription, resource group, and environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :type event_source_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    :type api_version: str
    :param event_source_update_parameters: Request object that contains the updated information for the event source.
    :type event_source_update_parameters: dict | bytes

    """
    event_source_update_parameters = EventSourceUpdateParameters.from_dict(event_source_update_parameters)
    return web.Response(status=200)
