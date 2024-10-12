# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event import Event
from openapi_server.models.events_count import EventsCount


pytestmark = pytest.mark.asyncio

async def test_get_event(client):
    """Test case for get_event

    Get event
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/events/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_count(client):
    """Test case for get_events_count

    Get events count
    """
    params = [('fromDate', 56),
                    ('toDate', 56),
                    ('direction', 'INBOUND,OUTBOUND'),
                    ('states', 'ACTIVE,RINGING')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/events/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_events(client):
    """Test case for list_events

    List events
    """
    params = [('types', 'CALL'),
                    ('fromDate', 56),
                    ('toDate', 56),
                    ('direction', 'INBOUND,OUTBOUND'),
                    ('states', 'ACTIVE,RINGING'),
                    ('offset', 56),
                    ('size', 20),
                    ('order', ASC),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

