# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_acknowledge_orders(client):
    """Test case for acknowledge_orders

    Acknowledge orders
    """
    params = [('shipNode', 'ship_node_example')]
    headers = { 
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='POST',
        path='/orderProxy/order-api-doc-app/rest/v3/orders/{purchase_order_id}/acknowledge'.format(purchase_order_id='purchase_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_cancel_order(client):
    """Test case for cancel_order

    Cancel order lines
    """
    request_body = 'request_body_example'
    params = [('shipNode', 'ship_node_example')]
    headers = { 
        'Content-Type': 'application/xml',
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='POST',
        path='/orderProxy/order-api-doc-app/rest/v3/orders/{purchase_order_id}/cancel'.format(purchase_order_id='purchase_order_id_example'),
        headers=headers,
        json=request_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_orders(client):
    """Test case for get_all_orders

    Get all orders
    """
    params = [('shipNode', 'ship_node_example'),
                    ('sku', 'sku_example'),
                    ('customerOrderId', 'customer_order_id_example'),
                    ('purchaseOrderId', 'purchase_order_id_example'),
                    ('status', 'status_example'),
                    ('createdStartDate', 'created_start_date_example'),
                    ('createdEndDate', 'created_end_date_example'),
                    ('fromExpectedShipDate', 'from_expected_ship_date_example'),
                    ('toExpectedShipDate', 'to_expected_ship_date_example'),
                    ('limit', 10)]
    headers = { 
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='GET',
        path='/orderProxy/order-api-doc-app/rest/v3/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_orders_next(client):
    """Test case for get_all_orders_next

    Get orders for next page
    """
    headers = { 
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='GET',
        path='/orderProxy/order-api-doc-app/rest/v3/orders{nextCursor}'.format(next_cursor='next_cursor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_next_cursor_released_orders(client):
    """Test case for get_next_cursor_released_orders

    Get released orders for next page
    """
    headers = { 
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='GET',
        path='/orderProxy/order-api-doc-app/rest/v3/orders/released{nextCursor}'.format(next_cursor='next_cursor_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_by_purchase_order_id(client):
    """Test case for get_order_by_purchase_order_id

    Get an order
    """
    params = [('shipNode', 'ship_node_example')]
    headers = { 
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='GET',
        path='/orderProxy/order-api-doc-app/rest/v3/orders/{purchase_order_id}'.format(purchase_order_id='purchase_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_released_orders(client):
    """Test case for get_released_orders

    Get all released orders
    """
    params = [('shipNode', 'ship_node_example'),
                    ('createdStartDate', 'created_start_date_example'),
                    ('limit', 56)]
    headers = { 
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='GET',
        path='/orderProxy/order-api-doc-app/rest/v3/orders/released',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_refund_order(client):
    """Test case for refund_order

    Refund order lines
    """
    request_body = 'request_body_example'
    params = [('shipNode', 'ship_node_example')]
    headers = { 
        'Content-Type': 'application/xml',
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='POST',
        path='/orderProxy/order-api-doc-app/rest/v3/orders/{purchase_order_id}/refund'.format(purchase_order_id='purchase_order_id_example'),
        headers=headers,
        json=request_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_shipping_order(client):
    """Test case for shipping_order

    Shipping updates
    """
    request_body = 'request_body_example'
    params = [('shipNode', 'ship_node_example')]
    headers = { 
        'Content-Type': 'application/xml',
        'content_type': application/xml,
        'accept': application/xml,
        'wm_consumer_channel_type': SWAGGER_CHANNEL_TYPE,
        'wm_consumer_id': 'wm_consumer_id_example',
        'wm_sec_timestamp': 'Auto populated',
        'wm_sec_auth_signature': 'Auto populated',
        'wm_svc_name': 'Walmart Marketplace',
        'wm_qos_correlation_id': '123456abcdef',
    }
    response = await client.request(
        method='POST',
        path='/orderProxy/order-api-doc-app/rest/v3/orders/{purchase_order_id}/shipping'.format(purchase_order_id='purchase_order_id_example'),
        headers=headers,
        json=request_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

