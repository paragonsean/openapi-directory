# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.managed_instance_administrator import ManagedInstanceAdministrator
from openapi_server.models.managed_instance_administrator_list_result import ManagedInstanceAdministratorListResult


pytestmark = pytest.mark.asyncio

async def test_managed_instance_administrators_create_or_update(client):
    """Test case for managed_instance_administrators_create_or_update

    
    """
    parameters = {"properties":{"administratorType":"ActiveDirectory","tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","login":"login","sid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/administrators/{administrator_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', administrator_name='administrator_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instance_administrators_delete(client):
    """Test case for managed_instance_administrators_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/administrators/{administrator_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', administrator_name='administrator_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instance_administrators_get(client):
    """Test case for managed_instance_administrators_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/administrators/{administrator_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', administrator_name='administrator_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instance_administrators_list_by_instance(client):
    """Test case for managed_instance_administrators_list_by_instance

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/administrators'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

