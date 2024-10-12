# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.order import Order
from openapi_server.models.order_list import OrderList


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Retrieve details for specified order
    """
    headers = { 
        'Accept': 'application/json',
        'x_shopper_id': 'x_shopper_id_example',
        'x_market_id': 'en-US',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders/{order_id}'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    Retrieve a list of orders for the authenticated shopper. Only one filter may be used at a time
    """
    params = [('periodStart', 'period_start_example'),
                    ('periodEnd', 'period_end_example'),
                    ('domain', 'domain_example'),
                    ('productGroupId', 56),
                    ('paymentProfileId', 56),
                    ('parentOrderId', 'parent_order_id_example'),
                    ('offset', 0),
                    ('limit', 25),
                    ('sort', -createdAt)]
    headers = { 
        'Accept': 'application/json',
        'x_shopper_id': 'x_shopper_id_example',
        'x_market_id': 'en-US',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

