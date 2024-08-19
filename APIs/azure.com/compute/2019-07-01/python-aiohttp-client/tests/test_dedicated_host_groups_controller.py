# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dedicated_host_group import DedicatedHostGroup
from openapi_server.models.dedicated_host_group_list_result import DedicatedHostGroupListResult
from openapi_server.models.dedicated_host_group_update import DedicatedHostGroupUpdate


pytestmark = pytest.mark.asyncio

async def test_dedicated_host_groups_create_or_update(client):
    """Test case for dedicated_host_groups_create_or_update

    
    """
    parameters = {"zones":["zones","zones"],"properties":{"platformFaultDomainCount":1,"hosts":[{"id":"id"},{"id":"id"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_host_groups_delete(client):
    """Test case for dedicated_host_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_host_groups_get(client):
    """Test case for dedicated_host_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_host_groups_list_by_resource_group(client):
    """Test case for dedicated_host_groups_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_host_groups_list_by_subscription(client):
    """Test case for dedicated_host_groups_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/hostGroups'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_host_groups_update(client):
    """Test case for dedicated_host_groups_update

    
    """
    parameters = {"zones":["zones","zones"],"properties":{"platformFaultDomainCount":1,"hosts":[{"id":"id"},{"id":"id"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

