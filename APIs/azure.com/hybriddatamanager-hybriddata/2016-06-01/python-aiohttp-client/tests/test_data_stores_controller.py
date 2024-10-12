# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_store import DataStore
from openapi_server.models.data_store_list import DataStoreList


pytestmark = pytest.mark.asyncio

async def test_data_stores_create_or_update(client):
    """Test case for data_stores_create_or_update

    
    """
    data_store = {"properties":{"extendedProperties":"{}","customerSecrets":[{"keyIdentifier":"keyIdentifier","keyValue":"keyValue","algorithm":"None"},{"keyIdentifier":"keyIdentifier","keyValue":"keyValue","algorithm":"None"}],"repositoryId":"repositoryId","dataStoreTypeId":"dataStoreTypeId","state":"Disabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataStores/{data_store_name}'.format(data_store_name='data_store_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        json=data_store,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_stores_delete(client):
    """Test case for data_stores_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataStores/{data_store_name}'.format(data_store_name='data_store_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_stores_get(client):
    """Test case for data_stores_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataStores/{data_store_name}'.format(data_store_name='data_store_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_stores_list_by_data_manager(client):
    """Test case for data_stores_list_by_data_manager

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HybridData/dataManagers/{data_manager_name}/dataStores'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', data_manager_name='data_manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

