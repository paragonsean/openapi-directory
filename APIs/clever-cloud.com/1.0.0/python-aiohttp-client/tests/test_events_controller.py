# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_events_event_socket_get_0(client):
    """Test case for events_event_socket_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/events/event-socket',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_info_events_get_0(client):
    """Test case for notifications_info_events_get_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/notifications/info/events',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

