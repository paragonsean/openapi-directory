# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event import Event


pytestmark = pytest.mark.asyncio

async def test_events_event_id_get(client):
    """Test case for events_event_id_get

    Returns an event
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/events/{event_id}'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

