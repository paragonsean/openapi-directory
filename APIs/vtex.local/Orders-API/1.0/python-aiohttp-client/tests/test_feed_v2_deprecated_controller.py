# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_getfeedorderstatus(client):
    """Test case for getfeedorderstatus

    Get feed order status
    """
    params = [('maxLot', '{{maxLot}}')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/pvt/feed/orders/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

