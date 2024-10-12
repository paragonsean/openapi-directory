# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.store_items import StoreItems


pytestmark = pytest.mark.asyncio

async def test_get_by_account(client):
    """Test case for get_by_account

    Get Stores
    """
    headers = { 
        'Accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/vlm/account/stores',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

