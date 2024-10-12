from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_secret_result import BackupSecretResult
from openapi_server.models.deleted_secret_bundle import DeletedSecretBundle
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.secret_bundle import SecretBundle
from openapi_server.models.secret_list_result import SecretListResult
from openapi_server.models.secret_restore_parameters import SecretRestoreParameters
from openapi_server.models.secret_set_parameters import SecretSetParameters
from openapi_server.models.secret_update_parameters import SecretUpdateParameters
from openapi_server import util


async def backup_secret(request: web.Request, secret_name, api_version) -> web.Response:
    """Backs up the specified secret.

    Requests that a backup of the specified secret be downloaded to the client. All versions of the secret will be downloaded. This operation requires the secrets/backup permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_secret(request: web.Request, secret_name, api_version) -> web.Response:
    """Deletes a secret from a specified key vault.

    The DELETE operation applies to any secret stored in Azure Key Vault. DELETE cannot be applied to an individual version of a secret. This operation requires the secrets/delete permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_secret(request: web.Request, secret_name, secret_version, api_version) -> web.Response:
    """Get a specified secret from a given key vault.

    The GET operation is applicable to any secret stored in Azure Key Vault. This operation requires the secrets/get permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param secret_version: The version of the secret.
    :type secret_version: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_secret_versions(request: web.Request, secret_name, api_version, maxresults=None) -> web.Response:
    """List all versions of the specified secret.

    The full secret identifier and attributes are provided in the response. No values are returned for the secrets. This operations requires the secrets/list permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def get_secrets(request: web.Request, api_version, maxresults=None) -> web.Response:
    """List secrets in a specified key vault.

    The Get Secrets operation is applicable to the entire vault. However, only the base secret identifier and its attributes are provided in the response. Individual secret versions are not listed in the response. This operation requires the secrets/list permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def restore_secret(request: web.Request, api_version, parameters) -> web.Response:
    """Restores a backed up secret to a vault.

    Restores a backed up secret, and all its versions, to a vault. This operation requires the secrets/restore permission.

    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to restore the secret.
    :type parameters: dict | bytes

    """
    parameters = SecretRestoreParameters.from_dict(parameters)
    return web.Response(status=200)


async def set_secret(request: web.Request, secret_name, api_version, parameters) -> web.Response:
    """Sets a secret in a specified key vault.

     The SET operation adds a secret to the Azure Key Vault. If the named secret already exists, Azure Key Vault creates a new version of that secret. This operation requires the secrets/set permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for setting the secret.
    :type parameters: dict | bytes

    """
    parameters = SecretSetParameters.from_dict(parameters)
    return web.Response(status=200)


async def update_secret(request: web.Request, secret_name, secret_version, api_version, parameters) -> web.Response:
    """Updates the attributes associated with a specified secret in a given key vault.

    The UPDATE operation changes specified attributes of an existing stored secret. Attributes that are not specified in the request are left unchanged. The value of a secret itself cannot be changed. This operation requires the secrets/set permission.

    :param secret_name: The name of the secret.
    :type secret_name: str
    :param secret_version: The version of the secret.
    :type secret_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for update secret operation.
    :type parameters: dict | bytes

    """
    parameters = SecretUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
