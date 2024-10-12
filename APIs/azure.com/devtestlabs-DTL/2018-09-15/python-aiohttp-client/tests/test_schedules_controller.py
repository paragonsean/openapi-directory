# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.schedule import Schedule
from openapi_server.models.schedule_fragment import ScheduleFragment
from openapi_server.models.schedule_list import ScheduleList


pytestmark = pytest.mark.asyncio

async def test_schedules_create_or_update(client):
    """Test case for schedules_create_or_update

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=schedule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_delete(client):
    """Test case for schedules_delete

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_execute(client):
    """Test case for schedules_execute

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/schedules/{name}/execute'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_get(client):
    """Test case for schedules_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_list(client):
    """Test case for schedules_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/schedules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_list_applicable(client):
    """Test case for schedules_list_applicable

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/schedules/{name}/listApplicable'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_update(client):
    """Test case for schedules_update

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/schedules/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=schedule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

