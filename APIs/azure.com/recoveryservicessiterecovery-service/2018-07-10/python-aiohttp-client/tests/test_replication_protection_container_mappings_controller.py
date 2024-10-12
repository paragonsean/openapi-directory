# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_protection_container_mapping_input import CreateProtectionContainerMappingInput
from openapi_server.models.protection_container_mapping import ProtectionContainerMapping
from openapi_server.models.protection_container_mapping_collection import ProtectionContainerMappingCollection
from openapi_server.models.remove_protection_container_mapping_input import RemoveProtectionContainerMappingInput
from openapi_server.models.update_protection_container_mapping_input import UpdateProtectionContainerMappingInput


pytestmark = pytest.mark.asyncio

async def test_replication_protection_container_mappings_create(client):
    """Test case for replication_protection_container_mappings_create

    Create protection container mapping.
    """
    creation_input = {"properties":{"policyId":"policyId","targetProtectionContainerId":"targetProtectionContainerId","providerSpecificInput":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectionContainerMappings/{mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', mapping_name='mapping_name_example'),
        headers=headers,
        json=creation_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protection_container_mappings_delete(client):
    """Test case for replication_protection_container_mappings_delete

    Remove protection container mapping.
    """
    removal_input = {"properties":{"providerSpecificInput":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectionContainerMappings/{mapping_name}/remove'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', mapping_name='mapping_name_example'),
        headers=headers,
        json=removal_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protection_container_mappings_get(client):
    """Test case for replication_protection_container_mappings_get

    Gets a protection container mapping/
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectionContainerMappings/{mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', mapping_name='mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protection_container_mappings_list(client):
    """Test case for replication_protection_container_mappings_list

    Gets the list of all protection container mappings in a vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationProtectionContainerMappings'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protection_container_mappings_list_by_replication_protection_containers(client):
    """Test case for replication_protection_container_mappings_list_by_replication_protection_containers

    Gets the list of protection container mappings for a protection container.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectionContainerMappings'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protection_container_mappings_purge(client):
    """Test case for replication_protection_container_mappings_purge

    Purge protection container mapping.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectionContainerMappings/{mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', mapping_name='mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protection_container_mappings_update(client):
    """Test case for replication_protection_container_mappings_update

    Update protection container mapping.
    """
    update_input = {"properties":{"providerSpecificInput":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectionContainerMappings/{mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', mapping_name='mapping_name_example'),
        headers=headers,
        json=update_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

