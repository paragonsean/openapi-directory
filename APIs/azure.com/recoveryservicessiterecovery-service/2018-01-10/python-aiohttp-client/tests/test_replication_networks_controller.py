# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.network import Network
from openapi_server.models.network_collection import NetworkCollection


pytestmark = pytest.mark.asyncio

async def test_replication_networks_get(client):
    """Test case for replication_networks_get

    Gets a network with specified server id and network name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationNetworks/{network_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', network_name='network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_networks_list(client):
    """Test case for replication_networks_list

    Gets the list of networks. View-only API.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationNetworks'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_networks_list_by_replication_fabrics(client):
    """Test case for replication_networks_list_by_replication_fabrics

    Gets the list of networks under a fabric.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationNetworks'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

