# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.public_key import PublicKey
from openapi_server.models.public_key_list import PublicKeyList


pytestmark = pytest.mark.asyncio

async def test_public_keys_get(client):
    """Test case for public_keys_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/publicKeys/{public_key_name}'.format(public_key_name='public_key_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_keys_list_by_data_manager(client):
    """Test case for public_keys_list_by_data_manager

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/publicKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

