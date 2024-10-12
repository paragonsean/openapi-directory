# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_mapping_input import CreateNetworkMappingInput
from openapi_server.models.network_mapping import NetworkMapping
from openapi_server.models.network_mapping_collection import NetworkMappingCollection
from openapi_server.models.update_network_mapping_input import UpdateNetworkMappingInput


pytestmark = pytest.mark.asyncio

async def test_replication_network_mappings_create(client):
    """Test case for replication_network_mappings_create

    Creates network mapping.
    """
    input = {"properties":{"recoveryNetworkId":"recoveryNetworkId","fabricSpecificDetails":{"instanceType":"instanceType"},"recoveryFabricName":"recoveryFabricName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationNetworks/{network_name}/replicationNetworkMappings/{network_mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', network_name='network_name_example', network_mapping_name='network_mapping_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_network_mappings_delete(client):
    """Test case for replication_network_mappings_delete

    Delete network mapping.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationNetworks/{network_name}/replicationNetworkMappings/{network_mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', network_name='network_name_example', network_mapping_name='network_mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_network_mappings_get(client):
    """Test case for replication_network_mappings_get

    Gets network mapping by name.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationNetworks/{network_name}/replicationNetworkMappings/{network_mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', network_name='network_name_example', network_mapping_name='network_mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_network_mappings_list(client):
    """Test case for replication_network_mappings_list

    Gets all the network mappings under a vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationNetworkMappings'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_network_mappings_list_by_replication_networks(client):
    """Test case for replication_network_mappings_list_by_replication_networks

    Gets all the network mappings under a network.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationNetworks/{network_name}/replicationNetworkMappings'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', network_name='network_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_network_mappings_update(client):
    """Test case for replication_network_mappings_update

    Updates network mapping.
    """
    input = {"properties":{"recoveryNetworkId":"recoveryNetworkId","fabricSpecificDetails":{"instanceType":"instanceType"},"recoveryFabricName":"recoveryFabricName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationNetworks/{network_name}/replicationNetworkMappings/{network_mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', network_name='network_name_example', network_mapping_name='network_mapping_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

