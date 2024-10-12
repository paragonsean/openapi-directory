# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_schedule import BackupSchedule
from openapi_server.models.backup_schedule_list import BackupScheduleList


pytestmark = pytest.mark.asyncio

async def test_backup_schedules_create_or_update(client):
    """Test case for backup_schedules_create_or_update

    
    """
    parameters = {"properties":{"scheduleRecurrence":{"recurrenceValue":6,"weeklyDaysList":["Sunday","Sunday"],"recurrenceType":"Minutes"},"retentionCount":0,"scheduleStatus":"Enabled","startTime":"2000-01-23T04:56:07.000+00:00","lastSuccessfulRun":"2000-01-23T04:56:07.000+00:00","backupType":"LocalSnapshot"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupPolicies/{backup_policy_name}/schedules/{backup_schedule_name}'.format(device_name='device_name_example', backup_policy_name='backup_policy_name_example', backup_schedule_name='backup_schedule_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_schedules_delete(client):
    """Test case for backup_schedules_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupPolicies/{backup_policy_name}/schedules/{backup_schedule_name}'.format(device_name='device_name_example', backup_policy_name='backup_policy_name_example', backup_schedule_name='backup_schedule_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_schedules_get(client):
    """Test case for backup_schedules_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupPolicies/{backup_policy_name}/schedules/{backup_schedule_name}'.format(device_name='device_name_example', backup_policy_name='backup_policy_name_example', backup_schedule_name='backup_schedule_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_schedules_list_by_backup_policy(client):
    """Test case for backup_schedules_list_by_backup_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/backupPolicies/{backup_policy_name}/schedules'.format(device_name='device_name_example', backup_policy_name='backup_policy_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

