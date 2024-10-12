# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_capacities_entity import EventsCapacitiesEntity


pytestmark = pytest.mark.asyncio

async def test_fetch_all_events_capacities(client):
    """Test case for fetch_all_events_capacities

    Find all capacities for one event
    """
    params = [('show_ignored', False),
                    ('sort', date),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/capacities'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_event_capacity(client):
    """Test case for fetch_one_event_capacity

    Get one capacity by ID
    """
    params = [('show_ignored', False)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/capacities/{capacity_id}'.format(event_id=56, capacity_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

