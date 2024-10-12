# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.schedule import Schedule
from openapi_server.models.schedule_request import ScheduleRequest


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_delete(client):
    """Test case for extractor_extractor_id_delete

    Delete an existing schedule
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/extractor/{extractor_id}'.format(extractor_id='extractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extractor_extractor_id_get(client):
    """Test case for extractor_extractor_id_get

    Get the schedule of a particular extractor
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/extractor/{extractor_id}'.format(extractor_id='extractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extractor_get(client):
    """Test case for extractor_get

    Get the list of schedules for all your extractors
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/extractor',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extractor_post(client):
    """Test case for extractor_post

    Schedule and extractor to run at a specific time
    """
    schedule_request_body = {"interval":"15 * * * *","extractorId":"00000000-0000-0000-0000-000000000000","startTimestamp":1485448509727}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/extractor',
        headers=headers,
        json=schedule_request_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

