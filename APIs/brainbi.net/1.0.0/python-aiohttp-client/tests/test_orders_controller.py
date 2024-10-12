# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_orders(client):
    """Test case for orders

    Orders
    """
    params = [('', '')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_orders1(client):
    """Test case for orders1

    Orders
    """
    params = [('', '')]
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='DELETE',
        path='/api/orders/1137',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

