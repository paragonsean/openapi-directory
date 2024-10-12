# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_customers(client):
    """Test case for customers

    Customers
    """
    params = [('', '')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

