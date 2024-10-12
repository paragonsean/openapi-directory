# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_payment_methods_get(client):
    """Test case for payment_methods_get

    Get list of payment methods
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/payment_methods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

