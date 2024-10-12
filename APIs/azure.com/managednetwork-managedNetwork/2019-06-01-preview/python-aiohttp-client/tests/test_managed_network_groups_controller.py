# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.managed_network_group import ManagedNetworkGroup
from openapi_server.models.managed_network_group_list_result import ManagedNetworkGroupListResult


pytestmark = pytest.mark.asyncio

async def test_managed_network_groups_create_or_update(client):
    """Test case for managed_network_groups_create_or_update

    
    """
    managed_network_group = {"kind":"Connectivity","properties":{"subscriptions":[{"id":"id"},{"id":"id"}],"managementGroups":[{"id":"id"},{"id":"id"}],"subnets":[{"id":"id"},{"id":"id"}],"virtualNetworks":[{"id":"id"},{"id":"id"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}/managedNetworkGroups/{managed_network_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example', managed_network_group_name='managed_network_group_name_example'),
        headers=headers,
        json=managed_network_group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_network_groups_delete(client):
    """Test case for managed_network_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}/managedNetworkGroups/{managed_network_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example', managed_network_group_name='managed_network_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_network_groups_get(client):
    """Test case for managed_network_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}/managedNetworkGroups/{managed_network_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example', managed_network_group_name='managed_network_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_network_groups_list_by_managed_network(client):
    """Test case for managed_network_groups_list_by_managed_network

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}/managedNetworkGroups'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

