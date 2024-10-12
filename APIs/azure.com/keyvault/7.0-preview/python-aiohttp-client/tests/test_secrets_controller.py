# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_secret_result import BackupSecretResult
from openapi_server.models.deleted_secret_bundle import DeletedSecretBundle
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.secret_bundle import SecretBundle
from openapi_server.models.secret_list_result import SecretListResult
from openapi_server.models.secret_restore_parameters import SecretRestoreParameters
from openapi_server.models.secret_set_parameters import SecretSetParameters
from openapi_server.models.secret_update_parameters import SecretUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_backup_secret(client):
    """Test case for backup_secret

    Backs up the specified secret.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/secrets/{secret_name}/backup'.format(secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_secret(client):
    """Test case for delete_secret

    Deletes a secret from a specified key vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/secrets/{secret_name}'.format(secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secret(client):
    """Test case for get_secret

    Get a specified secret from a given key vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/secrets/{secret_name}/{secret_version}'.format(secret_name='secret_name_example', secret_version='secret_version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secret_versions(client):
    """Test case for get_secret_versions

    List all versions of the specified secret.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/secrets/{secret_name}/versions'.format(secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secrets(client):
    """Test case for get_secrets

    List secrets in a specified key vault.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/secrets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_secret(client):
    """Test case for restore_secret

    Restores a backed up secret to a vault.
    """
    parameters = {"value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/secrets/restore',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_secret(client):
    """Test case for set_secret

    Sets a secret in a specified key vault.
    """
    parameters = {"attributes":{"recoveryLevel":"Purgeable"},"contentType":"contentType","value":"value","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/secrets/{secret_name}'.format(secret_name='secret_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_secret(client):
    """Test case for update_secret

    Updates the attributes associated with a specified secret in a given key vault.
    """
    parameters = {"attributes":{"recoveryLevel":"Purgeable"},"contentType":"contentType","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/secrets/{secret_name}/{secret_version}'.format(secret_name='secret_name_example', secret_version='secret_version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

