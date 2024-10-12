from typing import List, Dict
from aiohttp import web

from openapi_server.models.secret import Secret
from openapi_server.models.secret_create_or_update_parameters import SecretCreateOrUpdateParameters
from openapi_server.models.secret_list_result import SecretListResult
from openapi_server.models.secret_patch_parameters import SecretPatchParameters
from openapi_server import util


async def secrets_create_or_update(request: web.Request, resource_group_name, vault_name, secret_name, api_version, subscription_id, parameters) -> web.Response:
    """secrets_create_or_update

    Create or update a secret in a key vault in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param vault_name: Name of the vault
    :type vault_name: str
    :param secret_name: Name of the secret
    :type secret_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to create or update the secret
    :type parameters: dict | bytes

    """
    parameters = SecretCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def secrets_get(request: web.Request, resource_group_name, vault_name, secret_name, api_version, subscription_id) -> web.Response:
    """secrets_get

    Gets the specified secret.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param vault_name: The name of the vault.
    :type vault_name: str
    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def secrets_list(request: web.Request, resource_group_name, vault_name, api_version, subscription_id, top=None) -> web.Response:
    """secrets_list

    The List operation gets information about the secrets in a vault.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param vault_name: The name of the vault.
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Maximum number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def secrets_update(request: web.Request, resource_group_name, vault_name, secret_name, api_version, subscription_id, parameters) -> web.Response:
    """secrets_update

    Update a secret in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments.  Users should use the data-plane REST service for interaction with vault secrets.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param vault_name: Name of the vault
    :type vault_name: str
    :param secret_name: Name of the secret
    :type secret_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to patch the secret
    :type parameters: dict | bytes

    """
    parameters = SecretPatchParameters.from_dict(parameters)
    return web.Response(status=200)
