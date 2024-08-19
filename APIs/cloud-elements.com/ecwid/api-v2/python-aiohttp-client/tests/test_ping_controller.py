# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pong import Pong


pytestmark = pytest.mark.asyncio

async def test_get_ping(client):
    """Test case for get_ping

    Ping the Element to confirm that the Hub Element has a heartbeat.  If the Element does not have a heartbeat, an error message will be returned.
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

