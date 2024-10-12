# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_payment_refund_response import GetPaymentRefundResponse
from openapi_server.models.list_payment_refunds_response import ListPaymentRefundsResponse
from openapi_server.models.refund_payment_request import RefundPaymentRequest
from openapi_server.models.refund_payment_response import RefundPaymentResponse


pytestmark = pytest.mark.asyncio

async def test_get_payment_refund(client):
    """Test case for get_payment_refund

    GetPaymentRefund
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/refunds/{refund_id}'.format(refund_id='refund_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payment_refunds(client):
    """Test case for list_payment_refunds

    ListPaymentRefunds
    """
    params = [('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('sort_order', 'sort_order_example'),
                    ('cursor', 'cursor_example'),
                    ('location_id', 'location_id_example'),
                    ('status', 'status_example'),
                    ('source_type', 'source_type_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/refunds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refund_payment(client):
    """Test case for refund_payment

    RefundPayment
    """
    body = {"request_body":{"amount_money":{"amount":100,"currency":"USD"},"idempotency_key":"a7e36d40-d24b-11e8-b568-0800200c9a66","payment_id":"UNOE3kv2BZwqHlJ830RCt5YCuaB"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/refunds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

