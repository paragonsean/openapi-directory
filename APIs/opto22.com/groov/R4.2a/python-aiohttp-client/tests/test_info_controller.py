# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.groov_info import GroovInfo


pytestmark = pytest.mark.asyncio

async def test_groov_info(client):
    """Test case for groov_info

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

