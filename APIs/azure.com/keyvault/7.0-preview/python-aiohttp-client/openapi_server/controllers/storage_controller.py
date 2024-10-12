from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_storage_result import BackupStorageResult
from openapi_server.models.deleted_sas_definition_bundle import DeletedSasDefinitionBundle
from openapi_server.models.deleted_storage_bundle import DeletedStorageBundle
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.sas_definition_bundle import SasDefinitionBundle
from openapi_server.models.sas_definition_create_parameters import SasDefinitionCreateParameters
from openapi_server.models.sas_definition_list_result import SasDefinitionListResult
from openapi_server.models.sas_definition_update_parameters import SasDefinitionUpdateParameters
from openapi_server.models.storage_account_create_parameters import StorageAccountCreateParameters
from openapi_server.models.storage_account_regenerte_key_parameters import StorageAccountRegenerteKeyParameters
from openapi_server.models.storage_account_update_parameters import StorageAccountUpdateParameters
from openapi_server.models.storage_bundle import StorageBundle
from openapi_server.models.storage_list_result import StorageListResult
from openapi_server.models.storage_restore_parameters import StorageRestoreParameters
from openapi_server import util


async def backup_storage_account(request: web.Request, storage_account_name, api_version) -> web.Response:
    """Backs up the specified storage account.

    Requests that a backup of the specified storage account be downloaded to the client. This operation requires the storage/backup permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_sas_definition(request: web.Request, storage_account_name, sas_definition_name, api_version) -> web.Response:
    """delete_sas_definition

    Deletes a SAS definition from a specified storage account. This operation requires the storage/deletesas permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param sas_definition_name: The name of the SAS definition.
    :type sas_definition_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_storage_account(request: web.Request, storage_account_name, api_version) -> web.Response:
    """delete_storage_account

    Deletes a storage account. This operation requires the storage/delete permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_sas_definition(request: web.Request, storage_account_name, sas_definition_name, api_version) -> web.Response:
    """get_sas_definition

    Gets information about a SAS definition for the specified storage account. This operation requires the storage/getsas permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param sas_definition_name: The name of the SAS definition.
    :type sas_definition_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_sas_definitions(request: web.Request, storage_account_name, api_version, maxresults=None) -> web.Response:
    """get_sas_definitions

    List storage SAS definitions for the given storage account. This operation requires the storage/listsas permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def get_storage_account(request: web.Request, storage_account_name, api_version) -> web.Response:
    """get_storage_account

    Gets information about a specified storage account. This operation requires the storage/get permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_storage_accounts(request: web.Request, api_version, maxresults=None) -> web.Response:
    """get_storage_accounts

    List storage accounts managed by the specified key vault. This operation requires the storage/list permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def regenerate_storage_account_key(request: web.Request, storage_account_name, api_version, parameters) -> web.Response:
    """regenerate_storage_account_key

    Regenerates the specified key value for the given storage account. This operation requires the storage/regeneratekey permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to regenerate storage account key.
    :type parameters: dict | bytes

    """
    parameters = StorageAccountRegenerteKeyParameters.from_dict(parameters)
    return web.Response(status=200)


async def restore_storage_account(request: web.Request, api_version, parameters) -> web.Response:
    """Restores a backed up storage account to a vault.

    Restores a backed up storage account to a vault. This operation requires the storage/restore permission.

    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to restore the storage account.
    :type parameters: dict | bytes

    """
    parameters = StorageRestoreParameters.from_dict(parameters)
    return web.Response(status=200)


async def set_sas_definition(request: web.Request, storage_account_name, sas_definition_name, api_version, parameters) -> web.Response:
    """set_sas_definition

    Creates or updates a new SAS definition for the specified storage account. This operation requires the storage/setsas permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param sas_definition_name: The name of the SAS definition.
    :type sas_definition_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to create a SAS definition.
    :type parameters: dict | bytes

    """
    parameters = SasDefinitionCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def set_storage_account(request: web.Request, storage_account_name, api_version, parameters) -> web.Response:
    """set_storage_account

    Creates or updates a new storage account. This operation requires the storage/set permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to create a storage account.
    :type parameters: dict | bytes

    """
    parameters = StorageAccountCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def update_sas_definition(request: web.Request, storage_account_name, sas_definition_name, api_version, parameters) -> web.Response:
    """update_sas_definition

    Updates the specified attributes associated with the given SAS definition. This operation requires the storage/setsas permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param sas_definition_name: The name of the SAS definition.
    :type sas_definition_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to update a SAS definition.
    :type parameters: dict | bytes

    """
    parameters = SasDefinitionUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def update_storage_account(request: web.Request, storage_account_name, api_version, parameters) -> web.Response:
    """update_storage_account

    Updates the specified attributes associated with the given storage account. This operation requires the storage/set/update permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to update a storage account.
    :type parameters: dict | bytes

    """
    parameters = StorageAccountUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
