# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_store_get(client):
    """Test case for store_get

    Get Fortnite Store
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/store',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

