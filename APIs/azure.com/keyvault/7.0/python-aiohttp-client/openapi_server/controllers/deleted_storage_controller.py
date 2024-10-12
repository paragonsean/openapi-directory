from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_sas_definition_bundle import DeletedSasDefinitionBundle
from openapi_server.models.deleted_sas_definition_list_result import DeletedSasDefinitionListResult
from openapi_server.models.deleted_storage_bundle import DeletedStorageBundle
from openapi_server.models.deleted_storage_list_result import DeletedStorageListResult
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.sas_definition_bundle import SasDefinitionBundle
from openapi_server.models.storage_bundle import StorageBundle
from openapi_server import util


async def get_deleted_sas_definition(request: web.Request, storage_account_name, sas_definition_name, api_version) -> web.Response:
    """Gets the specified deleted sas definition.

    The Get Deleted SAS Definition operation returns the specified deleted SAS definition along with its attributes. This operation requires the storage/getsas permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param sas_definition_name: The name of the SAS definition.
    :type sas_definition_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_deleted_sas_definitions(request: web.Request, storage_account_name, api_version, maxresults=None) -> web.Response:
    """Lists deleted SAS definitions for the specified vault and storage account.

    The Get Deleted Sas Definitions operation returns the SAS definitions that have been deleted for a vault enabled for soft-delete. This operation requires the storage/listsas permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def get_deleted_storage_account(request: web.Request, storage_account_name, api_version) -> web.Response:
    """Gets the specified deleted storage account.

    The Get Deleted Storage Account operation returns the specified deleted storage account along with its attributes. This operation requires the storage/get permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_deleted_storage_accounts(request: web.Request, api_version, maxresults=None) -> web.Response:
    """Lists deleted storage accounts for the specified vault.

    The Get Deleted Storage Accounts operation returns the storage accounts that have been deleted for a vault enabled for soft-delete. This operation requires the storage/list permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def purge_deleted_storage_account(request: web.Request, storage_account_name, api_version) -> web.Response:
    """Permanently deletes the specified storage account.

    The purge deleted storage account operation removes the secret permanently, without the possibility of recovery. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/purge permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def recover_deleted_sas_definition(request: web.Request, storage_account_name, sas_definition_name, api_version) -> web.Response:
    """Recovers the deleted SAS definition.

    Recovers the deleted SAS definition for the specified storage account. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/recover permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param sas_definition_name: The name of the SAS definition.
    :type sas_definition_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def recover_deleted_storage_account(request: web.Request, storage_account_name, api_version) -> web.Response:
    """Recovers the deleted storage account.

    Recovers the deleted storage account in the specified vault. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/recover permission.

    :param storage_account_name: The name of the storage account.
    :type storage_account_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
