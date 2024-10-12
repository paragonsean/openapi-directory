# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.behavioral_event_http_completion_request import BehavioralEventHttpCompletionRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_post_events_v3_send_send(client):
    """Test case for post_events_v3_send_send

    Send custom event completion
    """
    body = {"occurredAt":"2000-01-23T04:56:07.000+00:00","eventName":"eventName","utk":"utk","uuid":"uuid","email":"email","objectId":"objectId","properties":{"key":"properties"}}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/events/v3/send',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

