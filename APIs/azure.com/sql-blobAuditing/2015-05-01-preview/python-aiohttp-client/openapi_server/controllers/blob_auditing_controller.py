from typing import List, Dict
from aiohttp import web

from openapi_server.models.database_blob_auditing_policy import DatabaseBlobAuditingPolicy
from openapi_server.models.database_blob_auditing_policy_list_result import DatabaseBlobAuditingPolicyListResult
from openapi_server import util


async def database_blob_auditing_policies_create_or_update(request: web.Request, resource_group_name, server_name, database_name, blob_auditing_policy_name, subscription_id, api_version, parameters) -> web.Response:
    """database_blob_auditing_policies_create_or_update

    Creates or updates a database&#39;s blob auditing policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param blob_auditing_policy_name: The name of the blob auditing policy.
    :type blob_auditing_policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The database blob auditing policy.
    :type parameters: dict | bytes

    """
    parameters = DatabaseBlobAuditingPolicy.from_dict(parameters)
    return web.Response(status=200)


async def database_blob_auditing_policies_get(request: web.Request, resource_group_name, server_name, database_name, blob_auditing_policy_name, subscription_id, api_version) -> web.Response:
    """database_blob_auditing_policies_get

    Gets a database&#39;s blob auditing policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param blob_auditing_policy_name: The name of the blob auditing policy.
    :type blob_auditing_policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_blob_auditing_policies_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """database_blob_auditing_policies_list_by_database

    Lists auditing settings of a database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
