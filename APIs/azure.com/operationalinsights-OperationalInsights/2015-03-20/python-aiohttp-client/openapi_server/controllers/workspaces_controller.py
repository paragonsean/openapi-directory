from typing import List, Dict
from aiohttp import web

from openapi_server.models.link_target import LinkTarget
from openapi_server.models.search_get_schema_response import SearchGetSchemaResponse
from openapi_server.models.shared_keys import SharedKeys
from openapi_server.models.workspace_purge_body import WorkspacePurgeBody
from openapi_server.models.workspace_purge_response import WorkspacePurgeResponse
from openapi_server.models.workspace_purge_status_response import WorkspacePurgeStatusResponse
from openapi_server import util


async def workspaces_delete_gateways(request: web.Request, subscription_id, resource_group_name, workspace_name, gateway_id, api_version) -> web.Response:
    """workspaces_delete_gateways

    Delete a Log Analytics gateway.

    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param gateway_id: The Log Analytics gateway Id.
    :type gateway_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workspaces_get_purge_status(request: web.Request, resource_group_name, api_version, subscription_id, workspace_name, purge_id) -> web.Response:
    """workspaces_get_purge_status

    Gets status of an ongoing purge operation.

    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param purge_id: In a purge status request, this is the Id of the operation the status of which is returned.
    :type purge_id: str

    """
    return web.Response(status=200)


async def workspaces_get_schema(request: web.Request, resource_group_name, workspace_name, api_version, subscription_id) -> web.Response:
    """workspaces_get_schema

    Gets the schema for a given workspace.

    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_list_keys(request: web.Request, subscription_id, resource_group_name, workspace_name, api_version) -> web.Response:
    """workspaces_list_keys

    Gets the shared keys for a Log Analytics Workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace.

    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workspaces_list_link_targets(request: web.Request, api_version, subscription_id) -> web.Response:
    """workspaces_list_link_targets

    Get a list of workspaces which the current user has administrator privileges and are not associated with an Azure Subscription. The subscriptionId parameter in the Url is ignored.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspaces_purge(request: web.Request, resource_group_name, api_version, subscription_id, workspace_name, body) -> web.Response:
    """workspaces_purge

    Purges data in an Log Analytics workspace by a set of user-defined filters.  In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.

    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param body: Describes the body of a request to purge data in a single table of an Log Analytics Workspace
    :type body: dict | bytes

    """
    body = WorkspacePurgeBody.from_dict(body)
    return web.Response(status=200)


async def workspaces_regenerate_shared_keys(request: web.Request, subscription_id, resource_group_name, workspace_name, api_version) -> web.Response:
    """workspaces_regenerate_shared_keys

    Regenerates the shared keys for a Log Analytics Workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace.

    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param resource_group_name: The Resource Group name.
    :type resource_group_name: str
    :param workspace_name: The Log Analytics Workspace name.
    :type workspace_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
