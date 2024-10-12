# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_manager import DataManager
from openapi_server.models.data_manager_list import DataManagerList
from openapi_server.models.data_manager_update_parameter import DataManagerUpdateParameter


pytestmark = pytest.mark.asyncio

async def test_data_managers_create(client):
    """Test case for data_managers_create

    
    """
    data_manager = {"etag":"etag"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        json=data_manager,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_managers_delete(client):
    """Test case for data_managers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_managers_get(client):
    """Test case for data_managers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_managers_list(client):
    """Test case for data_managers_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HybridData/dataManagers'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_managers_list_by_resource_group(client):
    """Test case for data_managers_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_managers_update(client):
    """Test case for data_managers_update

    
    """
    data_manager_update_parameter = {"sku":{"tier":"tier","name":"name"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        json=data_manager_update_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

