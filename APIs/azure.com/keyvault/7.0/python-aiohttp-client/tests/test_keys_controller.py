# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_backup_key(client):
    """Test case for backup_key

    Requests that a backup of the specified key be downloaded to the client.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/backup'.format(key_name='key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_key(client):
    """Test case for create_key

    Creates a new key, stores it, then returns key parameters and attributes to the client.
    """
    parameters = {"kty":"EC","crv":"P-256","key_ops":["encrypt","encrypt"],"attributes":{"recoveryLevel":"Purgeable"},"key_size":0,"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/create'.format(key_name='key_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_decrypt(client):
    """Test case for decrypt

    Decrypts a single block of encrypted data.
    """
    parameters = {"alg":"RSA-OAEP","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/{key_version}/decrypt'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_key(client):
    """Test case for delete_key

    Deletes a key of any type from storage in Azure Key Vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/keys/{key_name}'.format(key_name='key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_encrypt(client):
    """Test case for encrypt

    Encrypts an arbitrary sequence of bytes using an encryption key that is stored in a key vault.
    """
    parameters = {"alg":"RSA-OAEP","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/{key_version}/encrypt'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_key(client):
    """Test case for get_key

    Gets the public part of a stored key.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/keys/{key_name}/{key_version}'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_key_versions(client):
    """Test case for get_key_versions

    Retrieves a list of individual key versions with the same key name.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/keys/{key_name}/versions'.format(key_name='key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keys(client):
    """Test case for get_keys

    List keys in the specified vault.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_key(client):
    """Test case for import_key

    Imports an externally created key, stores it, and returns key parameters and attributes to the client.
    """
    parameters = {"Hsm":True,"attributes":{"recoveryLevel":"Purgeable"},"key":{"d":"d","e":"e","crv":"P-256","kid":"kid","key_hsm":"key_hsm","k":"k","dp":"dp","dq":"dq","n":"n","p":"p","kty":"EC","q":"q","key_ops":["key_ops","key_ops"],"qi":"qi","x":"x","y":"y"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/keys/{key_name}'.format(key_name='key_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_key(client):
    """Test case for restore_key

    Restores a backed up key to a vault.
    """
    parameters = {"value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/restore',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign(client):
    """Test case for sign

    Creates a signature from a digest using the specified key.
    """
    parameters = {"alg":"PS256","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/{key_version}/sign'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unwrap_key(client):
    """Test case for unwrap_key

    Unwraps a symmetric key using the specified key that was initially used for wrapping that key.
    """
    parameters = {"alg":"RSA-OAEP","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/{key_version}/unwrapkey'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_key(client):
    """Test case for update_key

    The update key operation changes specified attributes of a stored key and can be applied to any key type and key version stored in Azure Key Vault.
    """
    parameters = {"key_ops":["encrypt","encrypt"],"attributes":{"recoveryLevel":"Purgeable"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/keys/{key_name}/{key_version}'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify(client):
    """Test case for verify

    Verifies a signature using a specified key.
    """
    parameters = {"digest":"digest","alg":"PS256","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/{key_version}/verify'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wrap_key(client):
    """Test case for wrap_key

    Wraps a symmetric key using a specified key.
    """
    parameters = {"alg":"RSA-OAEP","value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/{key_version}/wrapkey'.format(key_name='key_name_example', key_version='key_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

