from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_policy_resource import ProtectionPolicyResource
from openapi_server import util


async def protection_policies_create_or_update(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name, parameters) -> web.Response:
    """protection_policies_create_or_update

    Creates or modifies a backup policy. This is an asynchronous operation. Status of the operation can be fetched  using GetPolicyOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param policy_name: Backup policy to be created.
    :type policy_name: str
    :param parameters: resource backup policy
    :type parameters: dict | bytes

    """
    parameters = ProtectionPolicyResource.from_dict(parameters)
    return web.Response(status=200)


async def protection_policies_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name) -> web.Response:
    """protection_policies_get

    Provides the details of the backup policies associated to Recovery Services Vault. This is an asynchronous  operation. Status of the operation can be fetched using GetPolicyOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param policy_name: Backup policy information to be fetched.
    :type policy_name: str

    """
    return web.Response(status=200)
