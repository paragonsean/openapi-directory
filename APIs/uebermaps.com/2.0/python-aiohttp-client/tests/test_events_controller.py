# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.event_editable import EventEditable
from openapi_server.models.map import Map


pytestmark = pytest.mark.asyncio

async def test_events_get(client):
    """Test case for events_get

    List your own events
    """
    params = [('timeframe_start', 'timeframe_start_example'),
                    ('timeframe_end', 'timeframe_end_example'),
                    ('bounds', 'bounds_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_id_delete(client):
    """Test case for events_id_delete

    Delete event
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/events/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_id_get(client):
    """Test case for events_id_get

    Get event
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/events/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_id_patch(client):
    """Test case for events_id_patch

    Update event
    """
    event = {"starts_at":"2000-01-23T04:56:07.000+00:00","user_id":703943,"description":"Very special event","lon":12.394328,"ends_at":"2000-01-23T04:56:07.000+00:00","time_zone":"Berlin","title":"20th anniversary event","lat":53.293493,"picture":"<BASE_64_ENCODED_STRING>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/events/{id}'.format(id=56),
        headers=headers,
        json=event,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_events_get(client):
    """Test case for spots_id_events_get

    List events for a given spot
    """
    params = [('timeframe_start', 'timeframe_start_example'),
                    ('timeframe_end', 'timeframe_end_example'),
                    ('bounds', 'bounds_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spots/{id}/events'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_events_post(client):
    """Test case for spots_id_events_post

    Create event
    """
    event = {"starts_at":"2000-01-23T04:56:07.000+00:00","user_id":703943,"description":"Very special event","lon":12.394328,"ends_at":"2000-01-23T04:56:07.000+00:00","time_zone":"Berlin","title":"20th anniversary event","lat":53.293493,"picture":"<BASE_64_ENCODED_STRING>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/spots/{id}/events'.format(id=56),
        headers=headers,
        json=event,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

