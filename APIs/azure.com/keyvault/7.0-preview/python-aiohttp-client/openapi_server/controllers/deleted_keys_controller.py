from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_key_bundle import DeletedKeyBundle
from openapi_server.models.deleted_key_list_result import DeletedKeyListResult
from openapi_server.models.key_bundle import KeyBundle
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server import util


async def get_deleted_key(request: web.Request, key_name, api_version) -> web.Response:
    """Gets the public part of a deleted key.

    The Get Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/get permission. 

    :param key_name: The name of the key.
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_deleted_keys(request: web.Request, api_version, maxresults=None) -> web.Response:
    """Lists the deleted keys in the specified vault.

    Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a deleted key. This operation includes deletion-specific information. The Get Deleted Keys operation is applicable for vaults enabled for soft-delete. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/list permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def purge_deleted_key(request: web.Request, key_name, api_version) -> web.Response:
    """Permanently deletes the specified key.

    The Purge Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/purge permission.

    :param key_name: The name of the key
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def recover_deleted_key(request: web.Request, key_name, api_version) -> web.Response:
    """Recovers the deleted key to its latest version.

    The Recover Deleted Key operation is applicable for deleted keys in soft-delete enabled vaults. It recovers the deleted key back to its latest version under /keys. An attempt to recover an non-deleted key will return an error. Consider this the inverse of the delete operation on soft-delete enabled vaults. This operation requires the keys/recover permission.

    :param key_name: The name of the deleted key.
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
