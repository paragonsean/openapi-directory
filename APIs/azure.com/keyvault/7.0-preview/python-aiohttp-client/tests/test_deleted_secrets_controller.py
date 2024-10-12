# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted_secret_bundle import DeletedSecretBundle
from openapi_server.models.deleted_secret_list_result import DeletedSecretListResult
from openapi_server.models.key_vault_error import KeyVaultError
from openapi_server.models.secret_bundle import SecretBundle


pytestmark = pytest.mark.asyncio

async def test_get_deleted_secret(client):
    """Test case for get_deleted_secret

    Gets the specified deleted secret.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedsecrets/{secret_name}'.format(secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deleted_secrets(client):
    """Test case for get_deleted_secrets

    Lists deleted secrets for the specified vault.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedsecrets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purge_deleted_secret(client):
    """Test case for purge_deleted_secret

    Permanently deletes the specified secret.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/deletedsecrets/{secret_name}'.format(secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_deleted_secret(client):
    """Test case for recover_deleted_secret

    Recovers the deleted secret to the latest version.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/deletedsecrets/{secret_name}/recover'.format(secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

