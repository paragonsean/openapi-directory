# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.file_service_items import FileServiceItems
from openapi_server.models.file_service_properties import FileServiceProperties


pytestmark = pytest.mark.asyncio

async def test_file_services_get_service_properties(client):
    """Test case for file_services_get_service_properties

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices/{file_services_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', file_services_name='file_services_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_services_list(client):
    """Test case for file_services_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_services_set_service_properties(client):
    """Test case for file_services_set_service_properties

    
    """
    parameters = {"sku":"{}","properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices/{file_services_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', file_services_name='file_services_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

