# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedule import Schedule
from openapi_server.models.schedules_api_response import SchedulesAPIResponse


pytestmark = pytest.mark.asyncio

async def test_id_delete_schedules(client):
    """Test case for id_delete_schedules

    Handle DELETE reqeuest for Schedules
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/user/schedules/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_schedules(client):
    """Test case for id_get_schedules

    Handle GET reqeuest for Schedules
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/schedules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_single_schedule(client):
    """Test case for id_get_single_schedule

    Handle GET reqeuest for Schedules
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/schedules/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_schedules(client):
    """Test case for id_post_schedules

    Handle POST reqeuest for Schedules
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/user/schedules',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

