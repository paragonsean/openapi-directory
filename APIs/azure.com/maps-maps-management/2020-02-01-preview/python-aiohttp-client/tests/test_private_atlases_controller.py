# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.maps_list_operations_default_response import MapsListOperationsDefaultResponse
from openapi_server.models.private_atlas import PrivateAtlas
from openapi_server.models.private_atlas_create_parameters import PrivateAtlasCreateParameters
from openapi_server.models.private_atlas_list import PrivateAtlasList
from openapi_server.models.private_atlas_update_parameters import PrivateAtlasUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_private_atlases_create_or_update(client):
    """Test case for private_atlases_create_or_update

    
    """
    private_atlas_create_parameters = {"location":"location","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Maps/accounts/{account_name}/privateAtlases/{private_atlas_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', private_atlas_name='private_atlas_name_example'),
        headers=headers,
        json=private_atlas_create_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_atlases_delete(client):
    """Test case for private_atlases_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Maps/accounts/{account_name}/privateAtlases/{private_atlas_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', private_atlas_name='private_atlas_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_atlases_get(client):
    """Test case for private_atlases_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Maps/accounts/{account_name}/privateAtlases/{private_atlas_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', private_atlas_name='private_atlas_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_atlases_list_by_account(client):
    """Test case for private_atlases_list_by_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Maps/accounts/{account_name}/privateAtlases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_atlases_update(client):
    """Test case for private_atlases_update

    
    """
    private_atlas_update_parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Maps/accounts/{account_name}/privateAtlases/{private_atlas_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', private_atlas_name='private_atlas_name_example'),
        headers=headers,
        json=private_atlas_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

