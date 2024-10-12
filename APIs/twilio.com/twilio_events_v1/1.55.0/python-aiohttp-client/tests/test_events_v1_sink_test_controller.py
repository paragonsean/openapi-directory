# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.events_v1_sink_sink_test import EventsV1SinkSinkTest


pytestmark = pytest.mark.asyncio

async def test_create_sink_test(client):
    """Test case for create_sink_test

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/Sinks/{sid}/Test'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

