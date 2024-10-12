# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_areas_get(client):
    """Test case for areas_get

    Lists the geographical areas (e.g. districts) that can be used to filter events.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/areas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_get(client):
    """Test case for events_get

    Lists road events
    """
    params = [('format', json),
                    ('status', ALL),
                    ('severity', 'MAJOR'),
                    ('jurisdiction', 'drivebc.ca'),
                    ('event_type', INCIDENT),
                    ('created', '>2015-09-01T12:00:00Z'),
                    ('updated', '>2015-09-01T12:00:00Z'),
                    ('road_name', 'Highway 99'),
                    ('area_id', 'drivebc.ca/1'),
                    ('bbox', '-130,48,-116,60')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jurisdiction_get(client):
    """Test case for jurisdiction_get

    Lists the jurisdictions publishing data through this Open511 API implementation
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jurisdiction',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jurisdictiongeography_get(client):
    """Test case for jurisdictiongeography_get

    Provides the geographical boundaries for all the jurisdictions.
    """
    params = [('format', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jurisdictiongeography',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

