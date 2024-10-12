# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.start_stream_request import StartStreamRequest
from openapi_server.models.start_stream_response import StartStreamResponse
from openapi_server.models.stop_stream_response import StopStreamResponse


pytestmark = pytest.mark.asyncio

async def test_start_stream(client):
    """Test case for start_stream

    Play an audio file into a call
    """
    body = {"level":"0.4","loop":0,"stream_url":["https://example.com/waiting.mp3"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/calls/{uuid}/stream'.format(uuid='63f61863-4a51-4f6b-86e1-46edebcf9356'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_stream(client):
    """Test case for stop_stream

    Stop playing an audio file into a call
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/calls/{uuid}/stream'.format(uuid='63f61863-4a51-4f6b-86e1-46edebcf9356'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

