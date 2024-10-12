from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.identity import Identity
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server.models.user_assigned_identities_list_result import UserAssignedIdentitiesListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists available operations for the Microsoft.ManagedIdentity provider

    :param api_version: Version of API to invoke.
    :type api_version: str

    """
    return web.Response(status=200)


async def user_assigned_identities_create_or_update(request: web.Request, subscription_id, resource_group_name, resource_name, api_version, parameters) -> web.Response:
    """user_assigned_identities_create_or_update

    Create or update an identity in the specified subscription and resource group.

    :param subscription_id: The Id of the Subscription to which the identity belongs.
    :type subscription_id: str
    :param resource_group_name: The name of the Resource Group to which the identity belongs.
    :type resource_group_name: str
    :param resource_name: The name of the identity resource.
    :type resource_name: str
    :param api_version: Version of API to invoke.
    :type api_version: str
    :param parameters: Parameters to create or update the identity
    :type parameters: dict | bytes

    """
    parameters = Identity.from_dict(parameters)
    return web.Response(status=200)


async def user_assigned_identities_delete(request: web.Request, subscription_id, resource_group_name, resource_name, api_version) -> web.Response:
    """user_assigned_identities_delete

    Deletes the identity.

    :param subscription_id: The Id of the Subscription to which the identity belongs.
    :type subscription_id: str
    :param resource_group_name: The name of the Resource Group to which the identity belongs.
    :type resource_group_name: str
    :param resource_name: The name of the identity resource.
    :type resource_name: str
    :param api_version: Version of API to invoke.
    :type api_version: str

    """
    return web.Response(status=200)


async def user_assigned_identities_get(request: web.Request, subscription_id, resource_group_name, resource_name, api_version) -> web.Response:
    """user_assigned_identities_get

    Gets the identity.

    :param subscription_id: The Id of the Subscription to which the identity belongs.
    :type subscription_id: str
    :param resource_group_name: The name of the Resource Group to which the identity belongs.
    :type resource_group_name: str
    :param resource_name: The name of the identity resource.
    :type resource_name: str
    :param api_version: Version of API to invoke.
    :type api_version: str

    """
    return web.Response(status=200)


async def user_assigned_identities_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """user_assigned_identities_list_by_resource_group

    Lists all the userAssignedIdentities available under the specified ResourceGroup.

    :param subscription_id: The Id of the Subscription to which the identity belongs.
    :type subscription_id: str
    :param resource_group_name: The name of the Resource Group to which the identity belongs.
    :type resource_group_name: str
    :param api_version: Version of API to invoke.
    :type api_version: str

    """
    return web.Response(status=200)


async def user_assigned_identities_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """user_assigned_identities_list_by_subscription

    Lists all the userAssignedIdentities available under the specified subscription.

    :param subscription_id: The Id of the Subscription to which the identity belongs.
    :type subscription_id: str
    :param api_version: Version of API to invoke.
    :type api_version: str

    """
    return web.Response(status=200)


async def user_assigned_identities_update(request: web.Request, subscription_id, resource_group_name, resource_name, api_version, parameters) -> web.Response:
    """user_assigned_identities_update

    Update an identity in the specified subscription and resource group.

    :param subscription_id: The Id of the Subscription to which the identity belongs.
    :type subscription_id: str
    :param resource_group_name: The name of the Resource Group to which the identity belongs.
    :type resource_group_name: str
    :param resource_name: The name of the identity resource.
    :type resource_name: str
    :param api_version: Version of API to invoke.
    :type api_version: str
    :param parameters: Parameters to update the identity
    :type parameters: dict | bytes

    """
    parameters = Identity.from_dict(parameters)
    return web.Response(status=200)
