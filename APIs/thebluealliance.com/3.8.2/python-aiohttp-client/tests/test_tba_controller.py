# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_status import APIStatus


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

