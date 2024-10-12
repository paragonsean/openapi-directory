from typing import List, Dict
from aiohttp import web

from openapi_server.models.linked_service import LinkedService
from openapi_server.models.linked_service_list_result import LinkedServiceListResult
from openapi_server import util


async def linked_services_create_or_update(request: web.Request, resource_group_name, workspace_name, linked_service_name, subscription_id, api_version, parameters) -> web.Response:
    """linked_services_create_or_update

    Create or update a linked service.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace that will contain the linkedServices resource
    :type workspace_name: str
    :param linked_service_name: Name of the linkedServices resource
    :type linked_service_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters required to create or update a linked service.
    :type parameters: dict | bytes

    """
    parameters = LinkedService.from_dict(parameters)
    return web.Response(status=200)


async def linked_services_delete(request: web.Request, resource_group_name, workspace_name, linked_service_name, api_version, subscription_id) -> web.Response:
    """linked_services_delete

    Deletes a linked service instance.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace that contains the linkedServices resource
    :type workspace_name: str
    :param linked_service_name: Name of the linked service.
    :type linked_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def linked_services_get(request: web.Request, resource_group_name, workspace_name, linked_service_name, api_version, subscription_id) -> web.Response:
    """linked_services_get

    Gets a linked service instance.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace that contains the linkedServices resource
    :type workspace_name: str
    :param linked_service_name: Name of the linked service.
    :type linked_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def linked_services_list_by_workspace(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """linked_services_list_by_workspace

    Gets the linked services instances in a workspace.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace that contains the linked services.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
