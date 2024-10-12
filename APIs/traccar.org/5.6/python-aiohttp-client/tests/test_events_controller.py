# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event import Event


pytestmark = pytest.mark.asyncio

async def test_events_id_get(client):
    """Test case for events_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/events/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

