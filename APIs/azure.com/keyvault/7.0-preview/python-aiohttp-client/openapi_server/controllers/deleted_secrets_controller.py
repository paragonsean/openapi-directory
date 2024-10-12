from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_secret_bundle import DeletedSecretBundle
from openapi_server.models.deleted_secret_list_result import DeletedSecretListResult
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.secret_bundle import SecretBundle
from openapi_server import util


async def get_deleted_secret(request: web.Request, secret_name, api_version) -> web.Response:
    """Gets the specified deleted secret.

    The Get Deleted Secret operation returns the specified deleted secret along with its attributes. This operation requires the secrets/get permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_deleted_secrets(request: web.Request, api_version, maxresults=None) -> web.Response:
    """Lists deleted secrets for the specified vault.

    The Get Deleted Secrets operation returns the secrets that have been deleted for a vault enabled for soft-delete. This operation requires the secrets/list permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def purge_deleted_secret(request: web.Request, secret_name, api_version) -> web.Response:
    """Permanently deletes the specified secret.

    The purge deleted secret operation removes the secret permanently, without the possibility of recovery. This operation can only be enabled on a soft-delete enabled vault. This operation requires the secrets/purge permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def recover_deleted_secret(request: web.Request, secret_name, api_version) -> web.Response:
    """Recovers the deleted secret to the latest version.

    Recovers the deleted secret in the specified vault. This operation can only be performed on a soft-delete enabled vault. This operation requires the secrets/recover permission.

    :param secret_name: The name of the deleted secret.
    :type secret_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
