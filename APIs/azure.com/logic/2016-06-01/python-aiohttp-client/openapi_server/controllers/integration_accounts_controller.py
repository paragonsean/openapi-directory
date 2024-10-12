from typing import List, Dict
from aiohttp import web

from openapi_server.models.callback_url import CallbackUrl
from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.integration_account import IntegrationAccount
from openapi_server.models.integration_account_list_result import IntegrationAccountListResult
from openapi_server.models.key_vault_key_collection import KeyVaultKeyCollection
from openapi_server.models.list_key_vault_keys_definition import ListKeyVaultKeysDefinition
from openapi_server.models.regenerate_action_parameter import RegenerateActionParameter
from openapi_server.models.tracking_events_definition import TrackingEventsDefinition
from openapi_server import util


async def integration_accounts_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, integration_account) -> web.Response:
    """integration_accounts_create_or_update

    Creates or updates an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param integration_account: The integration account.
    :type integration_account: dict | bytes

    """
    integration_account = IntegrationAccount.from_dict(integration_account)
    return web.Response(status=200)


async def integration_accounts_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version) -> web.Response:
    """integration_accounts_delete

    Deletes an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_accounts_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version) -> web.Response:
    """integration_accounts_get

    Gets an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_accounts_get_callback_url(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, parameters) -> web.Response:
    """integration_accounts_get_callback_url

    Gets the integration account callback URL.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param parameters: The callback URL parameters.
    :type parameters: dict | bytes

    """
    parameters = GetCallbackUrlParameters.from_dict(parameters)
    return web.Response(status=200)


async def integration_accounts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, top=None) -> web.Response:
    """integration_accounts_list_by_resource_group

    Gets a list of integration accounts by resource group.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int

    """
    return web.Response(status=200)


async def integration_accounts_list_by_subscription(request: web.Request, subscription_id, api_version, top=None) -> web.Response:
    """integration_accounts_list_by_subscription

    Gets a list of integration accounts by subscription.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int

    """
    return web.Response(status=200)


async def integration_accounts_list_key_vault_keys(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, list_key_vault_keys) -> web.Response:
    """integration_accounts_list_key_vault_keys

    Gets the integration account&#39;s Key Vault keys.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param list_key_vault_keys: The key vault parameters.
    :type list_key_vault_keys: dict | bytes

    """
    list_key_vault_keys = ListKeyVaultKeysDefinition.from_dict(list_key_vault_keys)
    return web.Response(status=200)


async def integration_accounts_log_tracking_events(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, log_tracking_events) -> web.Response:
    """integration_accounts_log_tracking_events

    Logs the integration account&#39;s tracking events.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param log_tracking_events: The callback URL parameters.
    :type log_tracking_events: dict | bytes

    """
    log_tracking_events = TrackingEventsDefinition.from_dict(log_tracking_events)
    return web.Response(status=200)


async def integration_accounts_regenerate_access_key(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, regenerate_access_key) -> web.Response:
    """integration_accounts_regenerate_access_key

    Regenerates the integration account access key.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param regenerate_access_key: The access key type.
    :type regenerate_access_key: dict | bytes

    """
    regenerate_access_key = RegenerateActionParameter.from_dict(regenerate_access_key)
    return web.Response(status=200)


async def integration_accounts_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, integration_account) -> web.Response:
    """integration_accounts_update

    Updates an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param integration_account: The integration account.
    :type integration_account: dict | bytes

    """
    integration_account = IntegrationAccount.from_dict(integration_account)
    return web.Response(status=200)
