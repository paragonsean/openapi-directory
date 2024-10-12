# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multiple_activation_key import MultipleActivationKey
from openapi_server.models.multiple_activation_key_list import MultipleActivationKeyList
from openapi_server.models.multiple_activation_key_update import MultipleActivationKeyUpdate


pytestmark = pytest.mark.asyncio

async def test_multiple_activation_keys_create(client):
    """Test case for multiple_activation_keys_create

    
    """
    multiple_activation_key = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multiple_activation_key_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', multiple_activation_key_name='multiple_activation_key_name_example'),
        headers=headers,
        json=multiple_activation_key,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_multiple_activation_keys_delete(client):
    """Test case for multiple_activation_keys_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multiple_activation_key_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', multiple_activation_key_name='multiple_activation_key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_multiple_activation_keys_get(client):
    """Test case for multiple_activation_keys_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multiple_activation_key_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', multiple_activation_key_name='multiple_activation_key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_multiple_activation_keys_list(client):
    """Test case for multiple_activation_keys_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.WindowsESU/multipleActivationKeys'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_multiple_activation_keys_list_by_resource_group(client):
    """Test case for multiple_activation_keys_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsESU/multipleActivationKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_multiple_activation_keys_update(client):
    """Test case for multiple_activation_keys_update

    
    """
    multiple_activation_key = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multiple_activation_key_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', multiple_activation_key_name='multiple_activation_key_name_example'),
        headers=headers,
        json=multiple_activation_key,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

