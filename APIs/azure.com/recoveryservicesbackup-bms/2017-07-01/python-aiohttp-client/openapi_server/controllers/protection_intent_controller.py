from typing import List, Dict
from aiohttp import web

from openapi_server.models.pre_validate_enable_backup_request import PreValidateEnableBackupRequest
from openapi_server.models.pre_validate_enable_backup_response import PreValidateEnableBackupResponse
from openapi_server.models.protection_intent_resource import ProtectionIntentResource
from openapi_server import util


async def protection_intent_create_or_update(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, intent_object_name, parameters) -> web.Response:
    """protection_intent_create_or_update

    Create Intent for Enabling backup of an item. This is a synchronous operation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backup item.
    :type fabric_name: str
    :param intent_object_name: Intent object name.
    :type intent_object_name: str
    :param parameters: resource backed up item
    :type parameters: dict | bytes

    """
    parameters = ProtectionIntentResource.from_dict(parameters)
    return web.Response(status=200)


async def protection_intent_delete(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, intent_object_name) -> web.Response:
    """protection_intent_delete

    Used to remove intent from an item

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the intent.
    :type fabric_name: str
    :param intent_object_name: Intent to be deleted.
    :type intent_object_name: str

    """
    return web.Response(status=200)


async def protection_intent_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, intent_object_name) -> web.Response:
    """protection_intent_get

    Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation,  call the GetItemOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backed up item.
    :type fabric_name: str
    :param intent_object_name: Backed up item name whose details are to be fetched.
    :type intent_object_name: str

    """
    return web.Response(status=200)


async def protection_intent_validate(request: web.Request, api_version, azure_region, subscription_id, parameters) -> web.Response:
    """It will validate followings  1. Vault capacity  2. VM is already protected  3. Any VM related configuration passed in properties.

    

    :param api_version: Client Api Version.
    :type api_version: str
    :param azure_region: Azure region to hit Api
    :type azure_region: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param parameters: Enable backup validation request on Virtual Machine
    :type parameters: dict | bytes

    """
    parameters = PreValidateEnableBackupRequest.from_dict(parameters)
    return web.Response(status=200)
