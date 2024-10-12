from typing import List, Dict
from aiohttp import web

from openapi_server.models.sync_full_schema_properties_list_result import SyncFullSchemaPropertiesListResult
from openapi_server.models.sync_member import SyncMember
from openapi_server.models.sync_member_list_result import SyncMemberListResult
from openapi_server import util


async def sync_members_create_or_update(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, sync_member_name, subscription_id, api_version, parameters) -> web.Response:
    """sync_members_create_or_update

    Creates or updates a sync member.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group on which the sync member is hosted.
    :type sync_group_name: str
    :param sync_member_name: The name of the sync member.
    :type sync_member_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested sync member resource state.
    :type parameters: dict | bytes

    """
    parameters = SyncMember.from_dict(parameters)
    return web.Response(status=200)


async def sync_members_delete(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, sync_member_name, subscription_id, api_version) -> web.Response:
    """sync_members_delete

    Deletes a sync member.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group on which the sync member is hosted.
    :type sync_group_name: str
    :param sync_member_name: The name of the sync member.
    :type sync_member_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_members_get(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, sync_member_name, subscription_id, api_version) -> web.Response:
    """sync_members_get

    Gets a sync member.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group on which the sync member is hosted.
    :type sync_group_name: str
    :param sync_member_name: The name of the sync member.
    :type sync_member_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_members_list_by_sync_group(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version) -> web.Response:
    """sync_members_list_by_sync_group

    Lists sync members in the given sync group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_members_list_member_schemas(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, sync_member_name, subscription_id, api_version) -> web.Response:
    """sync_members_list_member_schemas

    Gets a sync member database schema.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group on which the sync member is hosted.
    :type sync_group_name: str
    :param sync_member_name: The name of the sync member.
    :type sync_member_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_members_refresh_member_schema(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, sync_member_name, subscription_id, api_version) -> web.Response:
    """sync_members_refresh_member_schema

    Refreshes a sync member database schema.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group on which the sync member is hosted.
    :type sync_group_name: str
    :param sync_member_name: The name of the sync member.
    :type sync_member_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_members_update(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, sync_member_name, subscription_id, api_version, parameters) -> web.Response:
    """sync_members_update

    Updates an existing sync member.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group on which the sync member is hosted.
    :type sync_group_name: str
    :param sync_member_name: The name of the sync member.
    :type sync_member_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested sync member resource state.
    :type parameters: dict | bytes

    """
    parameters = SyncMember.from_dict(parameters)
    return web.Response(status=200)
