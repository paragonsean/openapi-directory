# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_calendar_event_response_request import CreateCalendarEventResponseRequest
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse


pytestmark = pytest.mark.asyncio

async def test_create_calendar_event_response(client):
    """Test case for create_calendar_event_response

    Create calendar event response
    """
    body = openapi_server.CreateCalendarEventResponseRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/calendar_event_response',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

