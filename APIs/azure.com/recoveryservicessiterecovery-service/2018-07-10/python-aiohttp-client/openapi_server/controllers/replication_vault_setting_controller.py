from typing import List, Dict
from aiohttp import web

from openapi_server.models.vault_setting import VaultSetting
from openapi_server.models.vault_setting_collection import VaultSettingCollection
from openapi_server.models.vault_setting_creation_input import VaultSettingCreationInput
from openapi_server import util


async def replication_vault_setting_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, vault_setting_name, input) -> web.Response:
    """Updates vault setting. A vault setting object is a singleton per vault and it is always present by default.

    The operation to configure vault setting.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param vault_setting_name: Vault setting name.
    :type vault_setting_name: str
    :param input: Vault setting creation input.
    :type input: dict | bytes

    """
    input = VaultSettingCreationInput.from_dict(input)
    return web.Response(status=200)


async def replication_vault_setting_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, vault_setting_name) -> web.Response:
    """Gets the vault setting.

    Gets the vault setting. This includes the Migration Hub connection settings.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param vault_setting_name: Vault setting name.
    :type vault_setting_name: str

    """
    return web.Response(status=200)


async def replication_vault_setting_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of vault setting.

    Gets the list of vault setting. This includes the Migration Hub connection settings.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
