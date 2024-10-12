# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.secret import Secret
from openapi_server.models.secret_create_or_update_parameters import SecretCreateOrUpdateParameters
from openapi_server.models.secret_list_result import SecretListResult
from openapi_server.models.secret_patch_parameters import SecretPatchParameters


pytestmark = pytest.mark.asyncio

async def test_secrets_create_or_update(client):
    """Test case for secrets_create_or_update

    
    """
    parameters = {"properties":{"secretUri":"secretUri","secretUriWithVersion":"secretUriWithVersion","attributes":{"nbf":1,"created":0,"exp":6,"updated":5,"enabled":True},"contentType":"contentType","value":"value"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}/secrets/{secret_name}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', secret_name='secret_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_get(client):
    """Test case for secrets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}/secrets/{secret_name}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', secret_name='secret_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_list(client):
    """Test case for secrets_list

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}/secrets'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_update(client):
    """Test case for secrets_update

    
    """
    parameters = {"properties":{"attributes":{"nbf":1,"created":0,"exp":6,"updated":5,"enabled":True},"contentType":"contentType","value":"value"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}/secrets/{secret_name}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', secret_name='secret_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

