# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.implementation_response import ImplementationResponse


pytestmark = pytest.mark.asyncio

async def test_api_implementation_read(client):
    """Test case for api_implementation_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/implementation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

