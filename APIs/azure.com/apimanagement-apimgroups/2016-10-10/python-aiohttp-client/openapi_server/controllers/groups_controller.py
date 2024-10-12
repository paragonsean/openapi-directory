from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_collection import GroupCollection
from openapi_server.models.group_contract import GroupContract
from openapi_server.models.group_create_parameters import GroupCreateParameters
from openapi_server.models.group_update_parameters import GroupUpdateParameters
from openapi_server.models.groups_get_default_response import GroupsGetDefaultResponse
from openapi_server import util


async def groups_create_or_update(request: web.Request, resource_group_name, service_name, group_id, api_version, subscription_id, parameters) -> web.Response:
    """groups_create_or_update

    Creates or Updates a group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = GroupCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def groups_delete(request: web.Request, resource_group_name, service_name, group_id, if_match, api_version, subscription_id) -> web.Response:
    """groups_delete

    Deletes specific group of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param if_match: ETag of the Group Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def groups_get(request: web.Request, resource_group_name, service_name, group_id, api_version, subscription_id) -> web.Response:
    """groups_get

    Gets the details of the group specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def groups_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """groups_list_by_service

    Lists a collection of groups defined within a service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | type        | eq, ne                 | N/A                                         |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def groups_update(request: web.Request, resource_group_name, service_name, group_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """groups_update

    Updates the details of the group specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param if_match: ETag of the Group Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = GroupUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
