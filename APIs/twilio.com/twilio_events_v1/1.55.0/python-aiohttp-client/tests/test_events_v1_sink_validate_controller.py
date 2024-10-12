# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.events_v1_sink_sink_validate import EventsV1SinkSinkValidate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sink_validate(client):
    """Test case for create_sink_validate

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'test_id': 'test_id_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Sinks/{sid}/Validate'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

