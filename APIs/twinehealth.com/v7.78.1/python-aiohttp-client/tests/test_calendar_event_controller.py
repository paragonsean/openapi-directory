# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_calendar_event_request import CreateCalendarEventRequest
from openapi_server.models.create_calendar_event_response import CreateCalendarEventResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_calendar_event_response import FetchCalendarEventResponse
from openapi_server.models.fetch_calendar_events_response import FetchCalendarEventsResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.update_calendar_event_request import UpdateCalendarEventRequest
from openapi_server.models.update_calendar_event_response import UpdateCalendarEventResponse


pytestmark = pytest.mark.asyncio

async def test_create_calendar_event(client):
    """Test case for create_calendar_event

    Create calendar event
    """
    body = openapi_server.CreateCalendarEventRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/calendar_event',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_calendar_event(client):
    """Test case for delete_calendar_event

    Delete a calendar event
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='DELETE',
        path='/pub/calendar_event/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_calendar_event(client):
    """Test case for fetch_calendar_event

    Get a calendar event
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/calendar_event/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_calendar_events(client):
    """Test case for fetch_calendar_events

    List calendar events
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example'),
                    ('filter[attendees]', 'filter_attendees_example'),
                    ('filter[type]', 'filter_type_example'),
                    ('filter[completed]', True),
                    ('filter[start_at]', 'filter_start_at_example'),
                    ('filter[end_at]', 'filter_end_at_example'),
                    ('filter[completed_at]', 'filter_completed_at_example'),
                    ('filter[created_at]', 'filter_created_at_example'),
                    ('filter[updated_at]', 'filter_updated_at_example'),
                    ('page[number]', 1),
                    ('page[size]', 10),
                    ('page[limit]', 50),
                    ('page[cursor]', 'page_cursor_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/calendar_event',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_calendar_event(client):
    """Test case for update_calendar_event

    Update a calendar event
    """
    body = openapi_server.UpdateCalendarEventRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='PATCH',
        path='/pub/calendar_event/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

