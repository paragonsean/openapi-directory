# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_grid_event import EventGridEvent


pytestmark = pytest.mark.asyncio

async def test_publish_events(client):
    """Test case for publish_events

    
    """
    events = {"data":"{}","dataVersion":"dataVersion","subject":"subject","eventTime":"2000-01-23T04:56:07.000+00:00","topic":"topic","eventType":"eventType","id":"id","metadataVersion":"metadataVersion"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/events',
        headers=headers,
        json=events,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

