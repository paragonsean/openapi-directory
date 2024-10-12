# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_user_schedule_request import CreateUserScheduleRequest
from openapi_server.models.schedule_template_collection import ScheduleTemplateCollection
from openapi_server.models.schedule_template_response import ScheduleTemplateResponse
from openapi_server.models.update_user_schedule_request import UpdateUserScheduleRequest
from openapi_server.models.user_schedule_collection import UserScheduleCollection
from openapi_server.models.user_schedule_response import UserScheduleResponse


pytestmark = pytest.mark.asyncio

async def test_create_schedule(client):
    """Test case for create_schedule

    
    """
    body = {"preferredTriggerDayOfWeek":"preferredTriggerDayOfWeek","scheduleName":"scheduleName","schemaVersion":"schemaVersion","scheduleTemplateId":"scheduleTemplateId","scheduleEndDate":"scheduleEndDate","scheduleStartDate":"scheduleStartDate","feedType":"feedType","preferredTriggerHour":"preferredTriggerHour","preferredTriggerDayOfMonth":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/feed/v1/schedule',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_schedule(client):
    """Test case for delete_schedule

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/feed/v1/schedule/{schedule_id}'.format(schedule_id='schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_result_file(client):
    """Test case for get_latest_result_file

    
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/schedule/{schedule_id}/download_result_file'.format(schedule_id='schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schedule(client):
    """Test case for get_schedule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/schedule/{schedule_id}'.format(schedule_id='schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schedule_template(client):
    """Test case for get_schedule_template

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/schedule_template/{schedule_template_id}'.format(schedule_template_id='schedule_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schedule_templates(client):
    """Test case for get_schedule_templates

    
    """
    params = [('feed_type', 'feed_type_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/schedule_template',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schedules(client):
    """Test case for get_schedules

    
    """
    params = [('feed_type', 'feed_type_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/schedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_schedule(client):
    """Test case for update_schedule

    
    """
    body = {"preferredTriggerDayOfWeek":"preferredTriggerDayOfWeek","scheduleName":"scheduleName","schemaVersion":"schemaVersion","scheduleEndDate":"scheduleEndDate","scheduleStartDate":"scheduleStartDate","preferredTriggerHour":"preferredTriggerHour","preferredTriggerDayOfMonth":0}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/feed/v1/schedule/{schedule_id}'.format(schedule_id='schedule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

