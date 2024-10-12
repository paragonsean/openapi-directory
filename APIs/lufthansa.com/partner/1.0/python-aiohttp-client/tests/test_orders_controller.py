# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_orders(client):
    """Test case for orders

    Orders
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders/orders/{order_id}/{name}'.format(order_id='order_id_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

