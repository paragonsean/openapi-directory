# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.events_event_id_get200_response import EventsEventIdGet200Response
from openapi_server.models.events_get200_response import EventsGet200Response
from openapi_server.models.events_is_user_free_get200_response import EventsIsUserFreeGet200Response
from openapi_server.models.events_post_request import EventsPostRequest


pytestmark = pytest.mark.asyncio

async def test_events_event_id_delete(client):
    """Test case for events_event_id_delete

    Delete event
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_event_id_get(client):
    """Test case for events_event_id_get

    Show event
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_event_id_put(client):
    """Test case for events_event_id_put

    Edit event
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_get(client):
    """Test case for events_get

    Show list of events
    """
    params = [('user_id', 'user_id_example'),
                    ('project_id', 'project_id_example'),
                    ('start[][gt]', 'start_gt_example'),
                    ('start[][lt]', 'start_lt_example'),
                    ('start[][eq]', 'start_eq_example'),
                    ('end[][gt]', 'end_gt_example'),
                    ('end[][lt]', 'end_lt_example'),
                    ('end[][eq]', 'end_eq_example'),
                    ('tags', 'tags_example'),
                    ('without_users', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_is_user_free_get(client):
    """Test case for events_is_user_free_get

    Check if user is available at given datetime range
    """
    params = [('user_id', 'user_id_example'),
                    ('start', 'start_example'),
                    ('end', 'end_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/is_user_free',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_post(client):
    """Test case for events_post

    Create event
    """
    body = openapi_server.EventsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/events',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

