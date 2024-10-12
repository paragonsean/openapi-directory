# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.retarget_schedule_properties import RetargetScheduleProperties
from openapi_server.models.schedule import Schedule
from openapi_server.models.schedule_fragment import ScheduleFragment
from openapi_server.models.schedule_list import ScheduleList


pytestmark = pytest.mark.asyncio

async def test_global_schedules_create_or_update(client):
    """Test case for global_schedules_create_or_update

    
    """
    schedule = {"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","createdDate":"2000-01-23T04:56:07.000+00:00","hourlyRecurrence":{"minute":0},"timeZoneId":"timeZoneId","provisioningState":"provisioningState","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":6,"notificationLocale":"notificationLocale","emailRecipient":"emailRecipient","webhookUrl":"webhookUrl","status":"Enabled"},"status":"Enabled","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=schedule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_schedules_delete(client):
    """Test case for global_schedules_delete

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_schedules_execute(client):
    """Test case for global_schedules_execute

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/schedules/{name}/execute'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_schedules_get(client):
    """Test case for global_schedules_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_schedules_list_by_resource_group(client):
    """Test case for global_schedules_list_by_resource_group

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/schedules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_schedules_list_by_subscription(client):
    """Test case for global_schedules_list_by_subscription

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DevTestLab/schedules'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_schedules_retarget(client):
    """Test case for global_schedules_retarget

    
    """
    retarget_schedule_properties = {"targetResourceId":"targetResourceId","currentResourceId":"currentResourceId"}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/schedules/{name}/retarget'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=retarget_schedule_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_schedules_update(client):
    """Test case for global_schedules_update

    
    """
    schedule = {"properties":{"dailyRecurrence":{"time":"time"},"targetResourceId":"targetResourceId","taskType":"taskType","hourlyRecurrence":{"minute":7},"timeZoneId":"timeZoneId","weeklyRecurrence":{"weekdays":["weekdays","weekdays"],"time":"time"},"notificationSettings":{"timeInMinutes":9,"notificationLocale":"notificationLocale","emailRecipient":"emailRecipient","webhookUrl":"webhookUrl","status":"Enabled"},"status":"Enabled"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', name='name_example'),
        headers=headers,
        json=schedule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

