# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.redis_patch_schedule import RedisPatchSchedule
from openapi_server.models.redis_patch_schedule_list_result import RedisPatchScheduleListResult


pytestmark = pytest.mark.asyncio

async def test_patch_schedules_create_or_update_0(client):
    """Test case for patch_schedules_create_or_update_0

    
    """
    parameters = {"properties":{"scheduleEntries":[{"maintenanceWindow":"maintenanceWindow","dayOfWeek":"Monday","startHourUtc":0},{"maintenanceWindow":"maintenanceWindow","dayOfWeek":"Monday","startHourUtc":0}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/{default}'.format(resource_group_name='resource_group_name_example', name='name_example', default='default_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_schedules_delete_0(client):
    """Test case for patch_schedules_delete_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/{default}'.format(resource_group_name='resource_group_name_example', name='name_example', default='default_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_schedules_get_0(client):
    """Test case for patch_schedules_get_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/{default}'.format(resource_group_name='resource_group_name_example', name='name_example', default='default_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_schedules_list_by_redis_resource_0(client):
    """Test case for patch_schedules_list_by_redis_resource_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Cache/Redis/{cache_name}/patchSchedules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cache_name='cache_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

