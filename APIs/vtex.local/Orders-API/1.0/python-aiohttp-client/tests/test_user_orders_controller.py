# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.userorderdetails import Userorderdetails
from openapi_server.models.userorderslist import Userorderslist


pytestmark = pytest.mark.asyncio

async def test_userorderdetails(client):
    """Test case for userorderdetails

    Retrieve user order details
    """
    params = [('clientEmail', 'customer@mail.com')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/user/orders/{order_id}'.format(order_id='1172452900788-01'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_userorderslist(client):
    """Test case for userorderslist

    Retrieve user's orders
    """
    params = [('clientEmail', 'customer@mail.com'),
                    ('page', '15'),
                    ('per_page', '15')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/user/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

