# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_health_check200_response import FetchHealthCheck200Response


pytestmark = pytest.mark.asyncio

async def test_fetch_health_check(client):
    """Test case for fetch_health_check

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/healthcheck',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

