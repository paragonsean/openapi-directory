# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server.models.volume_container import VolumeContainer
from openapi_server.models.volume_container_list import VolumeContainerList


pytestmark = pytest.mark.asyncio

async def test_volume_containers_create_or_update(client):
    """Test case for volume_containers_create_or_update

    
    """
    parameters = {"properties":{"bandWidthRateInMbps":0,"encryptionStatus":"Enabled","storageAccountCredentialId":"storageAccountCredentialId","ownerShipStatus":"Owned","volumeCount":1,"bandwidthSettingId":"bandwidthSettingId","encryptionKey":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"},"totalCloudStorageUsageInBytes":6}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/volumeContainers/{volume_container_name}'.format(device_name='device_name_example', volume_container_name='volume_container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_containers_delete(client):
    """Test case for volume_containers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/volumeContainers/{volume_container_name}'.format(device_name='device_name_example', volume_container_name='volume_container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_containers_get(client):
    """Test case for volume_containers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/volumeContainers/{volume_container_name}'.format(device_name='device_name_example', volume_container_name='volume_container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_containers_list_by_device(client):
    """Test case for volume_containers_list_by_device

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/volumeContainers'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_containers_list_metric_definition(client):
    """Test case for volume_containers_list_metric_definition

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/volumeContainers/{volume_container_name}/metricsDefinitions'.format(device_name='device_name_example', volume_container_name='volume_container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_containers_list_metrics(client):
    """Test case for volume_containers_list_metrics

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/volumeContainers/{volume_container_name}/metrics'.format(device_name='device_name_example', volume_container_name='volume_container_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

