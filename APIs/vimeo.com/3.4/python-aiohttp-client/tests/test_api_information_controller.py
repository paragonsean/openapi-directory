# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint import Endpoint


pytestmark = pytest.mark.asyncio

async def test_get_endpoints(client):
    """Test case for get_endpoints

    Get an API specification
    """
    params = [('openapi', true)]
    headers = { 
        'Accept': 'application/vnd.vimeo.endpoint+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

