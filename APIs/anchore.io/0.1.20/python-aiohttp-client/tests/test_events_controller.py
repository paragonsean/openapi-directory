# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.event_category import EventCategory
from openapi_server.models.event_response import EventResponse
from openapi_server.models.events_list import EventsList


pytestmark = pytest.mark.asyncio

async def test_delete_event(client):
    """Test case for delete_event

    Delete Event
    """
    headers = { 
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_events(client):
    """Test case for delete_events

    Delete Events
    """
    params = [('before', 'before_example'),
                    ('since', 'since_example'),
                    ('level', 'level_example')]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event(client):
    """Test case for get_event

    Get Event
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_event_types(client):
    """Test case for list_event_types

    List Event Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/event_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_events(client):
    """Test case for list_events

    List Events
    """
    params = [('source_servicename', 'source_servicename_example'),
                    ('source_hostid', 'source_hostid_example'),
                    ('event_type', 'event_type_example'),
                    ('resource_type', 'resource_type_example'),
                    ('resource_id', 'resource_id_example'),
                    ('level', 'level_example'),
                    ('since', 'since_example'),
                    ('before', 'before_example'),
                    ('page', 1),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

