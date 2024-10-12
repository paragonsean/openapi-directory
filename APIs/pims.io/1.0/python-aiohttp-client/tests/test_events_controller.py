# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_entity import EventsEntity


pytestmark = pytest.mark.asyncio

async def test_fetch_all_events(client):
    """Test case for fetch_all_events

    Find all events
    """
    params = [('label', 'label_example'),
                    ('from_datetime', '2013-10-20'),
                    ('to_datetime', '2013-10-20'),
                    ('city', 'city_example'),
                    ('sort', label),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_all_series_events(client):
    """Test case for fetch_all_series_events

    Find all events for one series
    """
    params = [('from_datetime', '2013-10-20'),
                    ('to_datetime', '2013-10-20'),
                    ('city', 'city_example'),
                    ('sort', label),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/series/{series_id}/events'.format(series_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_all_venues_events(client):
    """Test case for fetch_all_venues_events

    Find all events for one venue
    """
    params = [('from_datetime', '2013-10-20'),
                    ('to_datetime', '2013-10-20'),
                    ('city', 'city_example'),
                    ('sort', label),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/venues/{venue_id}/events'.format(venue_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_event(client):
    """Test case for fetch_one_event

    Get one event by ID
    """
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}'.format(event_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

