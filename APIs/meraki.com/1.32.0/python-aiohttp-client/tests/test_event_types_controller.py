# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_events_event_types200_response_inner import GetNetworkEventsEventTypes200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_events_event_types_2(client):
    """Test case for get_network_events_event_types_2

    List the event type to human-readable description
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/events/eventTypes'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

