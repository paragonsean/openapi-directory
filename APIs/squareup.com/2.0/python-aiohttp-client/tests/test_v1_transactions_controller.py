# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v1_create_refund_request import V1CreateRefundRequest
from openapi_server.models.v1_order import V1Order
from openapi_server.models.v1_payment import V1Payment
from openapi_server.models.v1_refund import V1Refund
from openapi_server.models.v1_settlement import V1Settlement
from openapi_server.models.v1_update_order_request import V1UpdateOrderRequest


pytestmark = pytest.mark.asyncio

async def test_create_refund(client):
    """Test case for create_refund

    CreateRefund
    """
    body = {"reason":"reason","request_idempotence_key":"request_idempotence_key","payment_id":"payment_id","refunded_money":{"amount":6,"currency_code":"currency_code"},"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{location_id}/refunds'.format(location_id='location_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_orders(client):
    """Test case for list_orders

    ListOrders
    """
    params = [('order', 'order_example'),
                    ('limit', 56),
                    ('batch_token', 'batch_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{location_id}/orders'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payments(client):
    """Test case for list_payments

    ListPayments
    """
    params = [('order', 'order_example'),
                    ('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('limit', 56),
                    ('batch_token', 'batch_token_example'),
                    ('include_partial', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{location_id}/payments'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_refunds(client):
    """Test case for list_refunds

    ListRefunds
    """
    params = [('order', 'order_example'),
                    ('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('limit', 56),
                    ('batch_token', 'batch_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{location_id}/refunds'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_settlements(client):
    """Test case for list_settlements

    ListSettlements
    """
    params = [('order', 'order_example'),
                    ('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('limit', 56),
                    ('status', 'status_example'),
                    ('batch_token', 'batch_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{location_id}/settlements'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_order(client):
    """Test case for retrieve_order

    RetrieveOrder
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{location_id}/orders/{order_id}'.format(location_id='location_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_payment(client):
    """Test case for retrieve_payment

    RetrievePayment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{location_id}/payments/{payment_id}'.format(location_id='location_id_example', payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_settlement(client):
    """Test case for retrieve_settlement

    RetrieveSettlement
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{location_id}/settlements/{settlement_id}'.format(location_id='location_id_example', settlement_id='settlement_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_order(client):
    """Test case for update_order

    UpdateOrder
    """
    body = {"completed_note":"completed_note","canceled_note":"canceled_note","shipped_tracking_number":"shipped_tracking_number","action":"action","refunded_note":"refunded_note"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{location_id}/orders/{order_id}'.format(location_id='location_id_example', order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

