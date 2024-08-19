# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_schedule_group import BackupScheduleGroup
from openapi_server.models.backup_schedule_group_list import BackupScheduleGroupList
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_backup_schedule_groups_create_or_update(client):
    """Test case for backup_schedule_groups_create_or_update

    
    """
    schedule_group = {"properties":{"startTime":{"hour":1,"minute":35}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupScheduleGroups/{schedule_group_name}'.format(device_name='device_name_example', schedule_group_name='schedule_group_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=schedule_group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_schedule_groups_delete(client):
    """Test case for backup_schedule_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupScheduleGroups/{schedule_group_name}'.format(device_name='device_name_example', schedule_group_name='schedule_group_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_schedule_groups_get(client):
    """Test case for backup_schedule_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupScheduleGroups/{schedule_group_name}'.format(device_name='device_name_example', schedule_group_name='schedule_group_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_schedule_groups_list_by_device(client):
    """Test case for backup_schedule_groups_list_by_device

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupScheduleGroups'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

