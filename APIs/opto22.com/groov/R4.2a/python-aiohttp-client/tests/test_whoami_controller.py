# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_who_am_i(client):
    """Test case for who_am_i

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/whoami',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

