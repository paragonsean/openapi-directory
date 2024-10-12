# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_classification_mapping import StorageClassificationMapping
from openapi_server.models.storage_classification_mapping_collection import StorageClassificationMappingCollection
from openapi_server.models.storage_classification_mapping_input import StorageClassificationMappingInput


pytestmark = pytest.mark.asyncio

async def test_replication_storage_classification_mappings_create(client):
    """Test case for replication_storage_classification_mappings_create

    Create storage classification mapping.
    """
    pairing_input = {"properties":{"targetStorageClassificationId":"targetStorageClassificationId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationStorageClassifications/{storage_classification_name}/replicationStorageClassificationMappings/{storage_classification_mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', storage_classification_name='storage_classification_name_example', storage_classification_mapping_name='storage_classification_mapping_name_example'),
        headers=headers,
        json=pairing_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_storage_classification_mappings_delete(client):
    """Test case for replication_storage_classification_mappings_delete

    Delete a storage classification mapping.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationStorageClassifications/{storage_classification_name}/replicationStorageClassificationMappings/{storage_classification_mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', storage_classification_name='storage_classification_name_example', storage_classification_mapping_name='storage_classification_mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_storage_classification_mappings_get(client):
    """Test case for replication_storage_classification_mappings_get

    Gets the details of a storage classification mapping.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationStorageClassifications/{storage_classification_name}/replicationStorageClassificationMappings/{storage_classification_mapping_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', storage_classification_name='storage_classification_name_example', storage_classification_mapping_name='storage_classification_mapping_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_storage_classification_mappings_list(client):
    """Test case for replication_storage_classification_mappings_list

    Gets the list of storage classification mappings objects under a vault.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationStorageClassificationMappings'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_storage_classification_mappings_list_by_replication_storage_classifications(client):
    """Test case for replication_storage_classification_mappings_list_by_replication_storage_classifications

    Gets the list of storage classification mappings objects under a storage.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationStorageClassifications/{storage_classification_name}/replicationStorageClassificationMappings'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', storage_classification_name='storage_classification_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

