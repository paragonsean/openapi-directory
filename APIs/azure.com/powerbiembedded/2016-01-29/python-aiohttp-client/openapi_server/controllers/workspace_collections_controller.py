from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_request import CheckNameRequest
from openapi_server.models.check_name_response import CheckNameResponse
from openapi_server.models.create_workspace_collection_request import CreateWorkspaceCollectionRequest
from openapi_server.models.error import Error
from openapi_server.models.migrate_workspace_collection_request import MigrateWorkspaceCollectionRequest
from openapi_server.models.update_workspace_collection_request import UpdateWorkspaceCollectionRequest
from openapi_server.models.workspace_collection import WorkspaceCollection
from openapi_server.models.workspace_collection_access_key import WorkspaceCollectionAccessKey
from openapi_server.models.workspace_collection_access_keys import WorkspaceCollectionAccessKeys
from openapi_server.models.workspace_collection_list import WorkspaceCollectionList
from openapi_server import util


async def workspace_collections_check_name_availability(request: web.Request, subscription_id, location, api_version, body) -> web.Response:
    """workspace_collections_check_name_availability

    Verify the specified Power BI Workspace Collection name is valid and not already in use.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Azure location
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param body: Check name availability request
    :type body: dict | bytes

    """
    body = CheckNameRequest.from_dict(body)
    return web.Response(status=200)


async def workspace_collections_create(request: web.Request, subscription_id, resource_group_name, workspace_collection_name, api_version, body) -> web.Response:
    """workspace_collections_create

    Creates a new Power BI Workspace Collection with the specified properties. A Power BI Workspace Collection contains one or more workspaces, and can be used to provision keys that provide API access to those workspaces.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param workspace_collection_name: Power BI Embedded Workspace Collection name
    :type workspace_collection_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param body: Create workspace collection request
    :type body: dict | bytes

    """
    body = CreateWorkspaceCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def workspace_collections_delete(request: web.Request, subscription_id, resource_group_name, workspace_collection_name, api_version) -> web.Response:
    """workspace_collections_delete

    Delete a Power BI Workspace Collection.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param workspace_collection_name: Power BI Embedded Workspace Collection name
    :type workspace_collection_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workspace_collections_get_access_keys(request: web.Request, subscription_id, resource_group_name, workspace_collection_name, api_version) -> web.Response:
    """workspace_collections_get_access_keys

    Retrieves the primary and secondary access keys for the specified Power BI Workspace Collection.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param workspace_collection_name: Power BI Embedded Workspace Collection name
    :type workspace_collection_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workspace_collections_get_by_name(request: web.Request, subscription_id, resource_group_name, workspace_collection_name, api_version) -> web.Response:
    """workspace_collections_get_by_name

    Retrieves an existing Power BI Workspace Collection.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param workspace_collection_name: Power BI Embedded Workspace Collection name
    :type workspace_collection_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workspace_collections_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """workspace_collections_list_by_resource_group

    Retrieves all existing Power BI workspace collections in the specified resource group.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workspace_collections_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """workspace_collections_list_by_subscription

    Retrieves all existing Power BI workspace collections in the specified subscription.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def workspace_collections_migrate(request: web.Request, subscription_id, resource_group_name, api_version, body) -> web.Response:
    """workspace_collections_migrate

    Migrates an existing Power BI Workspace Collection to a different resource group and/or subscription.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param body: Workspace migration request
    :type body: dict | bytes

    """
    body = MigrateWorkspaceCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def workspace_collections_regenerate_key(request: web.Request, subscription_id, resource_group_name, workspace_collection_name, api_version, body) -> web.Response:
    """workspace_collections_regenerate_key

    Regenerates the primary or secondary access key for the specified Power BI Workspace Collection.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param workspace_collection_name: Power BI Embedded Workspace Collection name
    :type workspace_collection_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param body: Access key to regenerate
    :type body: dict | bytes

    """
    body = WorkspaceCollectionAccessKey.from_dict(body)
    return web.Response(status=200)


async def workspace_collections_update(request: web.Request, subscription_id, resource_group_name, workspace_collection_name, api_version, body) -> web.Response:
    """workspace_collections_update

    Update an existing Power BI Workspace Collection with the specified properties.

    :param subscription_id: Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Azure resource group
    :type resource_group_name: str
    :param workspace_collection_name: Power BI Embedded Workspace Collection name
    :type workspace_collection_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param body: Update workspace collection request
    :type body: dict | bytes

    """
    body = UpdateWorkspaceCollectionRequest.from_dict(body)
    return web.Response(status=200)
