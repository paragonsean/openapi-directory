# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_endpoints200_response import GetEndpoints200Response
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_endpoints(client):
    """Test case for get_endpoints

    Get list of all endpoints
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

