from typing import List, Dict
from aiohttp import web

from openapi_server.models.enterprise_channel import EnterpriseChannel
from openapi_server.models.enterprise_channel_check_name_availability_request import EnterpriseChannelCheckNameAvailabilityRequest
from openapi_server.models.enterprise_channel_check_name_availability_response import EnterpriseChannelCheckNameAvailabilityResponse
from openapi_server.models.enterprise_channel_response_list import EnterpriseChannelResponseList
from openapi_server.models.error import Error
from openapi_server import util


async def enterprise_channels_check_name_availability(request: web.Request, api_version, parameters) -> web.Response:
    """enterprise_channels_check_name_availability

    Check whether an Enterprise Channel name is available.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The parameters to provide for the Enterprise Channel check name availability request.
    :type parameters: dict | bytes

    """
    parameters = EnterpriseChannelCheckNameAvailabilityRequest.from_dict(parameters)
    return web.Response(status=200)


async def enterprise_channels_create(request: web.Request, resource_group_name, resource_name, api_version, subscription_id, parameters) -> web.Response:
    """enterprise_channels_create

    Creates an Enterprise Channel.

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide for the new Enterprise Channel.
    :type parameters: dict | bytes

    """
    parameters = EnterpriseChannel.from_dict(parameters)
    return web.Response(status=200)


async def enterprise_channels_delete(request: web.Request, resource_group_name, resource_name, api_version, subscription_id) -> web.Response:
    """enterprise_channels_delete

    Deletes an Enterprise Channel from the resource group

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def enterprise_channels_get(request: web.Request, resource_group_name, resource_name, api_version, subscription_id) -> web.Response:
    """enterprise_channels_get

    Returns an Enterprise Channel specified by the parameters.

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def enterprise_channels_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """enterprise_channels_list_by_resource_group

    Returns all the resources of a particular type belonging to a resource group.

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def enterprise_channels_update(request: web.Request, resource_group_name, resource_name, api_version, subscription_id, parameters) -> web.Response:
    """enterprise_channels_update

    Updates an Enterprise Channel.

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide to update the Enterprise Channel.
    :type parameters: dict | bytes

    """
    parameters = EnterpriseChannel.from_dict(parameters)
    return web.Response(status=200)
