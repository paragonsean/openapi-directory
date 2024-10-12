# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_of_orders import ListOfOrders
from openapi_server.models.order import Order


pytestmark = pytest.mark.asyncio

async def test_orders_get(client):
    """Test case for orders_get

    List `orders`
    """
    params = [('orderStatus', 'order_status_example'),
                    ('offset', 'offset_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_order_id_get(client):
    """Test case for orders_order_id_get

    Get an `order`
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orders/{order_id}'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

