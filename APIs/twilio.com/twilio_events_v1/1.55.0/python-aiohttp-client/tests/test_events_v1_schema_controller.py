# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.events_v1_schema import EventsV1Schema


pytestmark = pytest.mark.asyncio

async def test_fetch_schema(client):
    """Test case for fetch_schema

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Schemas/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

