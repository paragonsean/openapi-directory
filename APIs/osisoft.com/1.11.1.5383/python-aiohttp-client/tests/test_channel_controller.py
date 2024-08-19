# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.items_channel_instance import ItemsChannelInstance


pytestmark = pytest.mark.asyncio

async def test_channel_instances(client):
    """Test case for channel_instances

    Retrieves a list of currently running channel instances.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/channels/instances',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

