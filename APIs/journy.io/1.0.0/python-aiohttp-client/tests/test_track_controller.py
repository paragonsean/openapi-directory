# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.track_event_request import TrackEventRequest


pytestmark = pytest.mark.asyncio

async def test_track_event(client):
    """Test case for track_event

    Track event
    """
    body = openapi_server.TrackEventRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/track',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

