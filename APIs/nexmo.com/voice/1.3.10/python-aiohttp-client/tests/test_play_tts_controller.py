# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.start_talk_request import StartTalkRequest
from openapi_server.models.start_talk_response import StartTalkResponse
from openapi_server.models.stop_talk_response import StopTalkResponse


pytestmark = pytest.mark.asyncio

async def test_start_talk(client):
    """Test case for start_talk

    Play text to speech into a call
    """
    body = {"premium":False,"level":"0.4","loop":0,"language":"en-US","style":6,"voice_name":"Kimberly","text":"Hello. How are you today?"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/calls/{uuid}/talk'.format(uuid='63f61863-4a51-4f6b-86e1-46edebcf9356'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_talk(client):
    """Test case for stop_talk

    Stop text to speech in a call
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/calls/{uuid}/talk'.format(uuid='63f61863-4a51-4f6b-86e1-46edebcf9356'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

