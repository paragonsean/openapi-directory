# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dtmf_request import DTMFRequest
from openapi_server.models.dtmf_response import DTMFResponse


pytestmark = pytest.mark.asyncio

async def test_start_dtmf(client):
    """Test case for start_dtmf

    Play DTMF tones into a call
    """
    body = {"digits":"1713"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/calls/{uuid}/dtmf'.format(uuid='63f61863-4a51-4f6b-86e1-46edebcf9356'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

