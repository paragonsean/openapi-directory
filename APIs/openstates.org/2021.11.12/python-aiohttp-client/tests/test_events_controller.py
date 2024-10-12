# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.event_include import EventInclude
from openapi_server.models.event_list import EventList
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_event_detail_events_event_id_get(client):
    """Test case for event_detail_events_event_id_get

    Event Detail
    """
    params = [('include', []),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_list_events_get(client):
    """Test case for event_list_events_get

    Event List
    """
    params = [('jurisdiction', 'jurisdiction_example'),
                    ('deleted', False),
                    ('before', 'before_example'),
                    ('after', 'after_example'),
                    ('require_bills', False),
                    ('include', []),
                    ('apikey', 'apikey_example'),
                    ('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

