# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transfer import Transfer


pytestmark = pytest.mark.asyncio

async def test_trasnfer(client):
    """Test case for trasnfer

    
    """
    body = openapi_server.Transfer()
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/api/transfer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

