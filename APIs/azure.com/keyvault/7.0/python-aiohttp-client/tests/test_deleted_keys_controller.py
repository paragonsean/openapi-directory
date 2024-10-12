# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted_key_bundle import DeletedKeyBundle
from openapi_server.models.deleted_key_list_result import DeletedKeyListResult
from openapi_server.models.key_bundle import KeyBundle
from openapi_server.models.key_vault_error import KeyVaultError


pytestmark = pytest.mark.asyncio

async def test_get_deleted_key(client):
    """Test case for get_deleted_key

    Gets the public part of a deleted key.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedkeys/{key_name}'.format(key_name='key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deleted_keys(client):
    """Test case for get_deleted_keys

    Lists the deleted keys in the specified vault.
    """
    params = [('maxresults', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/deletedkeys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purge_deleted_key(client):
    """Test case for purge_deleted_key

    Permanently deletes the specified key.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/deletedkeys/{key_name}'.format(key_name='key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_deleted_key(client):
    """Test case for recover_deleted_key

    Recovers the deleted key to its latest version.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/deletedkeys/{key_name}/recover'.format(key_name='key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

