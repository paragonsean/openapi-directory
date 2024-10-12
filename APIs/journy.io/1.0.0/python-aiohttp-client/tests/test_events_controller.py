# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.get_events200_response import GetEvents200Response
from openapi_server.models.track_journey_event_request import TrackJourneyEventRequest


pytestmark = pytest.mark.asyncio

async def test_get_events(client):
    """Test case for get_events

    Get events
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/events',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_track_journey_event(client):
    """Test case for track_journey_event

    Track event
    """
    body = openapi_server.TrackJourneyEventRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/events',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

