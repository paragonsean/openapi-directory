# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.event_occurence_detail import EventOccurenceDetail
from openapi_server.models.events_search_response import EventsSearchResponse


pytestmark = pytest.mark.asyncio

async def test_events_get(client):
    """Test case for events_get

    Find event occurrences in the area. Returns results at specific place and time, event groups are expanded for every occurrence.
    """
    params = [('category', ['category_example']),
                    ('activity', 'activity_example'),
                    ('ambience', 'ambience_example'),
                    ('genre', 'genre_example'),
                    ('name', 'name_example'),
                    ('q', 'q_example'),
                    ('from_day', 'from_day_example'),
                    ('to_day', 'to_day_example'),
                    ('capacity_min', 3.4),
                    ('capacity_max', 3.4),
                    ('center', 'center_example'),
                    ('radius', 56),
                    ('bbox', ['bbox_example']),
                    ('polygon', ['polygon_example']),
                    ('within', 'within_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('fieldset', context)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_id_get(client):
    """Test case for events_id_get

    Get Specific event details.
    """
    params = [('fieldset', summary)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/events/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

