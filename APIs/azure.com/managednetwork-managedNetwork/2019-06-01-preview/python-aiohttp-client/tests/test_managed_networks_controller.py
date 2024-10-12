# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.managed_network import ManagedNetwork
from openapi_server.models.managed_network_list_result import ManagedNetworkListResult
from openapi_server.models.managed_network_update import ManagedNetworkUpdate


pytestmark = pytest.mark.asyncio

async def test_managed_networks_create_or_update(client):
    """Test case for managed_networks_create_or_update

    
    """
    managed_network = {"properties":{"connectivity":{"groups":[{"kind":"Connectivity","properties":{"subscriptions":[{"id":"id"},{"id":"id"}],"managementGroups":[{"id":"id"},{"id":"id"}],"subnets":[{"id":"id"},{"id":"id"}],"virtualNetworks":[{"id":"id"},{"id":"id"}]}},{"kind":"Connectivity","properties":{"subscriptions":[{"id":"id"},{"id":"id"}],"managementGroups":[{"id":"id"},{"id":"id"}],"subnets":[{"id":"id"},{"id":"id"}],"virtualNetworks":[{"id":"id"},{"id":"id"}]}}],"peerings":[{"properties":{"hub":{"id":"id"},"spokes":[{"id":"id"},{"id":"id"}],"type":"HubAndSpokeTopology","mesh":[{"id":"id"},{"id":"id"}]}},{"properties":{"hub":{"id":"id"},"spokes":[{"id":"id"},{"id":"id"}],"type":"HubAndSpokeTopology","mesh":[{"id":"id"},{"id":"id"}]}}]},"scope":{"subscriptions":[{"id":"id"},{"id":"id"}],"managementGroups":[{"id":"id"},{"id":"id"}],"subnets":[{"id":"id"},{"id":"id"}],"virtualNetworks":[{"id":"id"},{"id":"id"}]}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example'),
        headers=headers,
        json=managed_network,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_networks_delete(client):
    """Test case for managed_networks_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_networks_get(client):
    """Test case for managed_networks_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_networks_list_by_resource_group(client):
    """Test case for managed_networks_list_by_resource_group

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_networks_list_by_subscription(client):
    """Test case for managed_networks_list_by_subscription

    
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.ManagedNetwork/managedNetworks'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_networks_update(client):
    """Test case for managed_networks_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ManagedNetwork/managedNetworks/{managed_network_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', managed_network_name='managed_network_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

