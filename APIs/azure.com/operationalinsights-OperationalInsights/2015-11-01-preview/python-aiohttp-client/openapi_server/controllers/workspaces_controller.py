from typing import List, Dict
from aiohttp import web

from openapi_server.models.intelligence_pack import IntelligencePack
from openapi_server.models.shared_keys import SharedKeys
from openapi_server.models.workspace import Workspace
from openapi_server.models.workspace_list_management_groups_result import WorkspaceListManagementGroupsResult
from openapi_server.models.workspace_list_result import WorkspaceListResult
from openapi_server.models.workspace_list_usages_result import WorkspaceListUsagesResult
from openapi_server import util


async def workspaces_create_or_update(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id, parameters) -> web.Response:
    """workspaces_create_or_update

    Create or update a workspace.

    :param resource_group_name: The resource group name of the workspace.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters required to create or update a workspace.
    :type parameters: dict | bytes

    """
    parameters = Workspace.from_dict(parameters)
    return web.Response(status=200)


async def workspaces_delete(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_delete

    Deletes a workspace instance.

    :param resource_group_name: The resource group name of the workspace.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_disable_intelligence_pack(request: web.Request, resource_group_name, workspace_name, intelligence_pack_name, api_version, subscription_id) -> web.Response:
    """workspaces_disable_intelligence_pack

    Disables an intelligence pack for a given workspace.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace.
    :type workspace_name: str
    :param intelligence_pack_name: The name of the intelligence pack to be disabled.
    :type intelligence_pack_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_enable_intelligence_pack(request: web.Request, resource_group_name, workspace_name, intelligence_pack_name, api_version, subscription_id) -> web.Response:
    """workspaces_enable_intelligence_pack

    Enables an intelligence pack for a given workspace.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace.
    :type workspace_name: str
    :param intelligence_pack_name: The name of the intelligence pack to be enabled.
    :type intelligence_pack_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_get(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_get

    Gets a workspace instance.

    :param resource_group_name: The resource group name of the workspace.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_get_shared_keys(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_get_shared_keys

    Gets the shared keys for a workspace.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """workspaces_list

    Gets the workspaces in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """workspaces_list_by_resource_group

    Gets workspaces in a resource group.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_intelligence_packs(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_list_intelligence_packs

    Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics Workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_management_groups(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_list_management_groups

    Gets a list of management groups connected to a workspace.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_usages(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_list_usages

    Gets a list of usage metrics for a workspace.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_update(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id, parameters) -> web.Response:
    """workspaces_update

    Updates a workspace.

    :param resource_group_name: The resource group name of the workspace.
    :type resource_group_name: str
    :param workspace_name: The name of the workspace.
    :type workspace_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters required to patch a workspace.
    :type parameters: dict | bytes

    """
    parameters = Workspace.from_dict(parameters)
    return web.Response(status=200)
