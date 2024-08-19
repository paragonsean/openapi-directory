# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.order import Order
from openapi_server.models.order_create import OrderCreate
from openapi_server.models.order_edit import OrderEdit
from openapi_server.models.order_history import OrderHistory
from openapi_server.models.order_history_edit import OrderHistoryEdit
from openapi_server.models.status_invalid import StatusInvalid


pytestmark = pytest.mark.asyncio

async def test_orders_after_id_json_get(client):
    """Test case for orders_after_id_json_get

    Retrieve orders filtered by Order Id.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders/after/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_count_json_get(client):
    """Test case for orders_count_json_get

    Count all Orders.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders/count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_id_history_json_get(client):
    """Test case for orders_id_history_json_get

    Retrieve all Order History.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders/{id}/history.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_id_history_json_post(client):
    """Test case for orders_id_history_json_post

    Create a new Order History Entry.
    """
    body = {"order_history":{"message":"message"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/orders/{id}/history.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_id_json_get(client):
    """Test case for orders_id_json_get

    Retrieve a single Order.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_id_json_put(client):
    """Test case for orders_id_json_put

    Modify an existing Order.
    """
    body = {"order":{"additional_information":"additional_information","tracking_number":"tracking_number","additional_fields":[{"label":"label","value":"value"},{"label":"label","value":"value"}],"tracking_company":"tracking_company","tracking_url":"tracking_url","shipment_status":"requested","status":"Abandoned"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/orders/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_json_get(client):
    """Test case for orders_json_get

    Retrieve all Orders.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('limit', 50),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_json_post(client):
    """Test case for orders_json_post

    Create a new Order.
    """
    body = {"order":{"shipping_price":9.301444,"shipping_method_id":7,"shipping_method_name":"shipping_method_name","customer":{"billing_address":{"country":"country","address":"address","city":"city","surname":"surname","taxid":"taxid","municipality":"municipality","name":"name","postal":"postal","region":"region"},"id":0,"shipping_address":{"country":"country","address":"address","city":"city","surname":"surname","municipality":"municipality","name":"name","postal":"postal","region":"region"}},"products":[{"variant_id":2,"price":5.962134,"qty":5,"discount":6.0274563,"id":1},{"variant_id":2,"price":5.962134,"qty":5,"discount":6.0274563,"id":1}],"status":"Abandoned"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/orders.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orders_status_status_json_get(client):
    """Test case for orders_status_status_json_get

    Retrieve orders filtered by status.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/orders/status/{status_jso}'.format(status='status_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

