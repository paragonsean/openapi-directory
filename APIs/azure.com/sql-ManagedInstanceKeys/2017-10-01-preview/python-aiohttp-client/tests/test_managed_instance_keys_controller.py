# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.managed_instance_key import ManagedInstanceKey
from openapi_server.models.managed_instance_key_list_result import ManagedInstanceKeyListResult


pytestmark = pytest.mark.asyncio

async def test_managed_instance_keys_create_or_update(client):
    """Test case for managed_instance_keys_create_or_update

    
    """
    parameters = {"kind":"kind","properties":{"serverKeyType":"ServiceManaged","thumbprint":"thumbprint","creationDate":"2000-01-23T04:56:07.000+00:00","uri":"uri"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/keys/{key_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', key_name='key_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instance_keys_delete(client):
    """Test case for managed_instance_keys_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/keys/{key_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', key_name='key_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instance_keys_get(client):
    """Test case for managed_instance_keys_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/keys/{key_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', key_name='key_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instance_keys_list_by_instance(client):
    """Test case for managed_instance_keys_list_by_instance

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/keys'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

