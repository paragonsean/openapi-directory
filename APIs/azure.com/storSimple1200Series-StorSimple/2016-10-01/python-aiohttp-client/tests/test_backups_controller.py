# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_list import BackupList
from openapi_server.models.clone_request import CloneRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_backups_clone(client):
    """Test case for backups_clone

    
    """
    clone_request = {"properties":{"disk":{"properties":{"localUsedCapacityInBytes":0,"accessControlRecords":["accessControlRecords","accessControlRecords"],"monitoringStatus":"Enabled","provisionedCapacityInBytes":6,"usedCapacityInBytes":1,"dataPolicy":"Invalid","description":"description","diskStatus":"Online"}},"newEndpointName":"newEndpointName","targetDeviceId":"targetDeviceId","targetAccessPointId":"targetAccessPointId","share":{"properties":{"localUsedCapacityInBytes":5,"adminUser":"adminUser","monitoringStatus":"Enabled","provisionedCapacityInBytes":5,"usedCapacityInBytes":2,"dataPolicy":"Invalid","description":"description","shareStatus":"Online"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backups/{backup_name}/elements/{element_name}/clone'.format(device_name='device_name_example', backup_name='backup_name_example', element_name='element_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=clone_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backups_delete(client):
    """Test case for backups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backups/{backup_name}'.format(device_name='device_name_example', backup_name='backup_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backups_list_by_device(client):
    """Test case for backups_list_by_device

    
    """
    params = [('forFailover', True),
                    ('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backups'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backups_list_by_manager(client):
    """Test case for backups_list_by_manager

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/backups'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

