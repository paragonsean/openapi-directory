# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_orders_order_id_feedback_buyer_get(client):
    """Test case for orders_order_id_feedback_buyer_get

    Feedback details for an order's buyer
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/orders/{order_id}/feedback/buyer'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_order_id_feedback_buyer_post(client):
    """Test case for orders_order_id_feedback_buyer_post

    Add feedback about an order's buyer
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/{order_id}/feedback/buyer'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_order_id_feedback_seller_get(client):
    """Test case for orders_order_id_feedback_seller_get

    Feedback details for an order's seller
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/orders/{order_id}/feedback/seller'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_order_id_feedback_seller_post(client):
    """Test case for orders_order_id_feedback_seller_post

    Add feedback about an order's seller
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/{order_id}/feedback/seller'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

