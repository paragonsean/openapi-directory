# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_retrieve_orders_request import BatchRetrieveOrdersRequest
from openapi_server.models.batch_retrieve_orders_response import BatchRetrieveOrdersResponse
from openapi_server.models.calculate_order_request import CalculateOrderRequest
from openapi_server.models.calculate_order_response import CalculateOrderResponse
from openapi_server.models.create_order_request import CreateOrderRequest
from openapi_server.models.create_order_response import CreateOrderResponse
from openapi_server.models.pay_order_request import PayOrderRequest
from openapi_server.models.pay_order_response import PayOrderResponse
from openapi_server.models.retrieve_order_response import RetrieveOrderResponse
from openapi_server.models.search_orders_request import SearchOrdersRequest
from openapi_server.models.search_orders_response import SearchOrdersResponse
from openapi_server.models.update_order_request import UpdateOrderRequest
from openapi_server.models.update_order_response import UpdateOrderResponse


pytestmark = pytest.mark.asyncio

async def test_batch_retrieve_orders(client):
    """Test case for batch_retrieve_orders

    BatchRetrieveOrders
    """
    body = {"request_body":{"location_id":"057P5VYJ4A5X1","order_ids":["CAISEM82RcpmcFBM0TfOyiHV3es","CAISENgvlJ6jLWAzERDzjyHVybY"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/orders/batch-retrieve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_order(client):
    """Test case for calculate_order

    CalculateOrder
    """
    body = {"request_body":{"idempotency_key":"b3e98fe3-b8de-471c-82f1-545f371e637c","order":{"discounts":[{"name":"50% Off","percentage":"50","scope":"ORDER"}],"line_items":[{"base_price_money":{"amount":500,"currency":"USD"},"name":"Item 1","quantity":"1"},{"base_price_money":{"amount":300,"currency":"USD"},"name":"Item 2","quantity":"2"}],"location_id":"D7AVYMEAPJ3A3"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/orders/calculate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_order(client):
    """Test case for create_order

    CreateOrder
    """
    body = {"request_body":{"idempotency_key":"8193148c-9586-11e6-99f9-28cfe92138cf","order":{"discounts":[{"name":"Labor Day Sale","percentage":"5","scope":"ORDER","uid":"labor-day-sale"},{"catalog_object_id":"DB7L55ZH2BGWI4H23ULIWOQ7","scope":"ORDER","uid":"membership-discount"},{"amount_money":{"amount":100,"currency":"USD"},"name":"Sale - $1.00 off","scope":"LINE_ITEM","uid":"one-dollar-off"}],"line_items":[{"base_price_money":{"amount":1599,"currency":"USD"},"name":"New York Strip Steak","quantity":"1"},{"applied_discounts":[{"discount_uid":"one-dollar-off"}],"catalog_object_id":"BEMYCSMIJL46OCDV4KYIKXIB","modifiers":[{"catalog_object_id":"CHQX7Y4KY6N5KINJKZCFURPZ"}],"quantity":"2"}],"location_id":"057P5VYJ4A5X1","reference_id":"my-order-001","taxes":[{"name":"State Sales Tax","percentage":"9","scope":"ORDER","uid":"state-sales-tax"}]}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/orders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pay_order(client):
    """Test case for pay_order

    PayOrder
    """
    body = {"request_body":{"idempotency_key":"c043a359-7ad9-4136-82a9-c3f1d66dcbff","payment_ids":["EnZdNAlWCmfh6Mt5FMNST1o7taB","0LRiVlbXVwe8ozu4KbZxd12mvaB"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/orders/{order_id}/pay'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_orders(client):
    """Test case for search_orders

    SearchOrders
    """
    body = {"request_body":{"limit":3,"location_ids":["057P5VYJ4A5X1","18YC4JDH91E1H"],"query":{"filter":{"date_time_filter":{"closed_at":{"end_at":"2019-03-04T21:54:45+00:00","start_at":"2018-03-03T20:00:00+00:00"}},"state_filter":{"states":["COMPLETED"]}},"sort":{"sort_field":"CLOSED_AT","sort_order":"DESC"}},"return_entries":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/orders/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_orders_order_id_get(client):
    """Test case for v2_orders_order_id_get

    RetrieveOrder
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/orders/{order_id}'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_orders_order_id_put(client):
    """Test case for v2_orders_order_id_put

    UpdateOrder
    """
    body = {"request_body":{"fields_to_clear":["discounts"],"idempotency_key":"UNIQUE_STRING","order":{"line_items":[{"base_price_money":{"amount":200,"currency":"USD"},"name":"COOKIE","quantity":"2","uid":"cookie_uid"}],"version":1}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/orders/{order_id}'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

