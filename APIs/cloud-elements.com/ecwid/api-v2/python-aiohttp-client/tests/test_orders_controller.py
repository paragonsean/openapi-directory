# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.order import Order
from openapi_server.models.order_patch import OrderPatch
from openapi_server.models.order_post import OrderPost
from openapi_server.models.payment import Payment


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_order(client):
    """Test case for create_order

    Create an order in the eCommerce system.With the exception of the 'id' field, the required fields indicated in the 'Order' model are those required to create a new order.The paymentStatus can only be AWAITING_PAYMENT or INCOMPLETE.The fulfillmentStatus can only be AWAITING_PROCESSING
    """
    order = openapi_server.OrderPost()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/elements/api-v2/orders',
        headers=headers,
        json=order,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_order_by_id(client):
    """Test case for delete_order_by_id

    Delete an order associated with a given ID from your eCommerce system. Specifying an order associated with a given ID that does not exist will result in an error message
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/elements/api-v2/orders/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_by_id(client):
    """Test case for get_order_by_id

    Retrieve an order associated with a given ID from the eCommerce system. Specifying an order with an ID that does not exist will result in an error response
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/orders/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_orders(client):
    """Test case for get_orders

    Find orders in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved
    """
    params = [('where', 'where_example'),
                    ('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_orders_payments(client):
    """Test case for get_orders_payments

    Retrieve the payments in the eCommerce system for the specified order
    """
    params = [('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/orders/{order_id}/payments'.format(order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_orders_refunds(client):
    """Test case for get_orders_refunds

    Retrieve the refunds in the eCommerce system for the specified order
    """
    params = [('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/orders/{order_id}/refunds'.format(order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_order_by_id(client):
    """Test case for update_order_by_id

    Update an order associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the order object will be updated, and those fields not provided will be left alone. Updating an order with a specified ID that does not exist will result in an error response</strong>
    """
    order = openapi_server.OrderPatch()
    params = [('action', 'action_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/elements/api-v2/orders/{id}'.format(id='id_example'),
        headers=headers,
        json=order,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

