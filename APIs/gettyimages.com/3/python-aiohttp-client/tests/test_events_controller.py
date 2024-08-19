# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_detail_field_values import EventDetailFieldValues


pytestmark = pytest.mark.asyncio

async def test_v3_events_get(client):
    """Test case for v3_events_get

    Get metadata for multiple events
    """
    params = [('ids', [56]),
                    ('fields', [openapi_server.EventDetailFieldValues()])]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_events_id_get(client):
    """Test case for v3_events_id_get

    Get metadata for a single event
    """
    params = [('fields', [openapi_server.EventDetailFieldValues()])]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/events/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

