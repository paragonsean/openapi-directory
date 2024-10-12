from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_key_result import BackupKeyResult
from openapi_server.models.deleted_key_bundle import DeletedKeyBundle
from openapi_server.models.key_bundle import KeyBundle
from openapi_server.models.key_create_parameters import KeyCreateParameters
from openapi_server.models.key_import_parameters import KeyImportParameters
from openapi_server.models.key_list_result import KeyListResult
from openapi_server.models.key_operation_result import KeyOperationResult
from openapi_server.models.key_operations_parameters import KeyOperationsParameters
from openapi_server.models.key_restore_parameters import KeyRestoreParameters
from openapi_server.models.key_sign_parameters import KeySignParameters
from openapi_server.models.key_update_parameters import KeyUpdateParameters
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.key_verify_parameters import KeyVerifyParameters
from openapi_server.models.key_verify_result import KeyVerifyResult
from openapi_server import util


async def backup_key(request: web.Request, key_name, api_version) -> web.Response:
    """Requests that a backup of the specified key be downloaded to the client.

    The Key Backup operation exports a key from Azure Key Vault in a protected form. Note that this operation does NOT return key material in a form that can be used outside the Azure Key Vault system, the returned key material is either protected to a Azure Key Vault HSM or to Azure Key Vault itself. The intent of this operation is to allow a client to GENERATE a key in one Azure Key Vault instance, BACKUP the key, and then RESTORE it into another Azure Key Vault instance. The BACKUP operation may be used to export, in protected form, any key type from Azure Key Vault. Individual versions of a key cannot be backed up. BACKUP / RESTORE can be performed within geographical boundaries only; meaning that a BACKUP from one geographical area cannot be restored to another geographical area. For example, a backup from the US geographical area cannot be restored in an EU geographical area. This operation requires the key/backup permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def create_key(request: web.Request, key_name, api_version, parameters) -> web.Response:
    """Creates a new key, stores it, then returns key parameters and attributes to the client.

    The create key operation can be used to create any key type in Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. It requires the keys/create permission.

    :param key_name: The name for the new key. The system will generate the version name for the new key.
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to create a key.
    :type parameters: dict | bytes

    """
    parameters = KeyCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def decrypt(request: web.Request, key_name, key_version, api_version, parameters) -> web.Response:
    """Decrypts a single block of encrypted data.

    The DECRYPT operation decrypts a well-formed block of ciphertext using the target encryption key and specified algorithm. This operation is the reverse of the ENCRYPT operation; only a single block of data may be decrypted, the size of this block is dependent on the target key and the algorithm to be used. The DECRYPT operation applies to asymmetric and symmetric keys stored in Azure Key Vault since it uses the private portion of the key. This operation requires the keys/decrypt permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param key_version: The version of the key.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for the decryption operation.
    :type parameters: dict | bytes

    """
    parameters = KeyOperationsParameters.from_dict(parameters)
    return web.Response(status=200)


async def delete_key(request: web.Request, key_name, api_version) -> web.Response:
    """Deletes a key of any type from storage in Azure Key Vault.

    The delete key operation cannot be used to remove individual versions of a key. This operation removes the cryptographic material associated with the key, which means the key is not usable for Sign/Verify, Wrap/Unwrap or Encrypt/Decrypt operations. This operation requires the keys/delete permission.

    :param key_name: The name of the key to delete.
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def encrypt(request: web.Request, key_name, key_version, api_version, parameters) -> web.Response:
    """Encrypts an arbitrary sequence of bytes using an encryption key that is stored in a key vault.

    The ENCRYPT operation encrypts an arbitrary sequence of bytes using an encryption key that is stored in Azure Key Vault. Note that the ENCRYPT operation only supports a single block of data, the size of which is dependent on the target key and the encryption algorithm to be used. The ENCRYPT operation is only strictly necessary for symmetric keys stored in Azure Key Vault since protection with an asymmetric key can be performed using public portion of the key. This operation is supported for asymmetric keys as a convenience for callers that have a key-reference but do not have access to the public key material. This operation requires the keys/encrypt permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param key_version: The version of the key.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for the encryption operation.
    :type parameters: dict | bytes

    """
    parameters = KeyOperationsParameters.from_dict(parameters)
    return web.Response(status=200)


async def get_key(request: web.Request, key_name, key_version, api_version) -> web.Response:
    """Gets the public part of a stored key.

    The get key operation is applicable to all key types. If the requested key is symmetric, then no key material is released in the response. This operation requires the keys/get permission.

    :param key_name: The name of the key to get.
    :type key_name: str
    :param key_version: Adding the version parameter retrieves a specific version of a key.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_key_versions(request: web.Request, key_name, api_version, maxresults=None) -> web.Response:
    """Retrieves a list of individual key versions with the same key name.

    The full key identifier, attributes, and tags are provided in the response. This operation requires the keys/list permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def get_keys(request: web.Request, api_version, maxresults=None) -> web.Response:
    """List keys in the specified vault.

    Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a stored key. The LIST operation is applicable to all key types, however only the base key identifier, attributes, and tags are provided in the response. Individual versions of a key are not listed in the response. This operation requires the keys/list permission.

    :param api_version: Client API version.
    :type api_version: str
    :param maxresults: Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    :type maxresults: int

    """
    return web.Response(status=200)


async def import_key(request: web.Request, key_name, api_version, parameters) -> web.Response:
    """Imports an externally created key, stores it, and returns key parameters and attributes to the client.

    The import key operation may be used to import any key type into an Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. This operation requires the keys/import permission.

    :param key_name: Name for the imported key.
    :type key_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to import a key.
    :type parameters: dict | bytes

    """
    parameters = KeyImportParameters.from_dict(parameters)
    return web.Response(status=200)


async def restore_key(request: web.Request, api_version, parameters) -> web.Response:
    """Restores a backed up key to a vault.

    Imports a previously backed up key into Azure Key Vault, restoring the key, its key identifier, attributes and access control policies. The RESTORE operation may be used to import a previously backed up key. Individual versions of a key cannot be restored. The key is restored in its entirety with the same key name as it had when it was backed up. If the key name is not available in the target Key Vault, the RESTORE operation will be rejected. While the key name is retained during restore, the final key identifier will change if the key is restored to a different vault. Restore will restore all versions and preserve version identifiers. The RESTORE operation is subject to security constraints: The target Key Vault must be owned by the same Microsoft Azure Subscription as the source Key Vault The user must have RESTORE permission in the target Key Vault. This operation requires the keys/restore permission.

    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters to restore the key.
    :type parameters: dict | bytes

    """
    parameters = KeyRestoreParameters.from_dict(parameters)
    return web.Response(status=200)


async def sign(request: web.Request, key_name, key_version, api_version, parameters) -> web.Response:
    """Creates a signature from a digest using the specified key.

    The SIGN operation is applicable to asymmetric and symmetric keys stored in Azure Key Vault since this operation uses the private portion of the key. This operation requires the keys/sign permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param key_version: The version of the key.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for the signing operation.
    :type parameters: dict | bytes

    """
    parameters = KeySignParameters.from_dict(parameters)
    return web.Response(status=200)


async def unwrap_key(request: web.Request, key_name, key_version, api_version, parameters) -> web.Response:
    """Unwraps a symmetric key using the specified key that was initially used for wrapping that key.

    The UNWRAP operation supports decryption of a symmetric key using the target key encryption key. This operation is the reverse of the WRAP operation. The UNWRAP operation applies to asymmetric and symmetric keys stored in Azure Key Vault since it uses the private portion of the key. This operation requires the keys/unwrapKey permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param key_version: The version of the key.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for the key operation.
    :type parameters: dict | bytes

    """
    parameters = KeyOperationsParameters.from_dict(parameters)
    return web.Response(status=200)


async def update_key(request: web.Request, key_name, key_version, api_version, parameters) -> web.Response:
    """The update key operation changes specified attributes of a stored key and can be applied to any key type and key version stored in Azure Key Vault.

    In order to perform this operation, the key must already exist in the Key Vault. Note: The cryptographic material of a key itself cannot be changed. This operation requires the keys/update permission.

    :param key_name: The name of key to update.
    :type key_name: str
    :param key_version: The version of the key to update.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters of the key to update.
    :type parameters: dict | bytes

    """
    parameters = KeyUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def verify(request: web.Request, key_name, key_version, api_version, parameters) -> web.Response:
    """Verifies a signature using a specified key.

    The VERIFY operation is applicable to symmetric keys stored in Azure Key Vault. VERIFY is not strictly necessary for asymmetric keys stored in Azure Key Vault since signature verification can be performed using the public portion of the key but this operation is supported as a convenience for callers that only have a key-reference and not the public portion of the key. This operation requires the keys/verify permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param key_version: The version of the key.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for verify operations.
    :type parameters: dict | bytes

    """
    parameters = KeyVerifyParameters.from_dict(parameters)
    return web.Response(status=200)


async def wrap_key(request: web.Request, key_name, key_version, api_version, parameters) -> web.Response:
    """Wraps a symmetric key using a specified key.

    The WRAP operation supports encryption of a symmetric key using a key encryption key that has previously been stored in an Azure Key Vault. The WRAP operation is only strictly necessary for symmetric keys stored in Azure Key Vault since protection with an asymmetric key can be performed using the public portion of the key. This operation is supported for asymmetric keys as a convenience for callers that have a key-reference but do not have access to the public key material. This operation requires the keys/wrapKey permission.

    :param key_name: The name of the key.
    :type key_name: str
    :param key_version: The version of the key.
    :type key_version: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: The parameters for wrap operation.
    :type parameters: dict | bytes

    """
    parameters = KeyOperationsParameters.from_dict(parameters)
    return web.Response(status=200)
