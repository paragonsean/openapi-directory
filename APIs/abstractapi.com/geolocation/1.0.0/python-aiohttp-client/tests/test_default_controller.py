# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response200 import InlineResponse200


pytestmark = pytest.mark.asyncio

async def test_v1_get(client):
    """Test case for v1_get

    
    """
    params = [('api_key', 'api_key_example'),
                    ('ip_address', '195.154.25.40'),
                    ('fields', 'country,city,timezone')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

