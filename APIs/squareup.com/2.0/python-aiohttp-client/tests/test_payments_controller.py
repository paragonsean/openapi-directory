# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_payment_by_idempotency_key_request import CancelPaymentByIdempotencyKeyRequest
from openapi_server.models.cancel_payment_by_idempotency_key_response import CancelPaymentByIdempotencyKeyResponse
from openapi_server.models.cancel_payment_response import CancelPaymentResponse
from openapi_server.models.complete_payment_response import CompletePaymentResponse
from openapi_server.models.create_payment_request import CreatePaymentRequest
from openapi_server.models.create_payment_response import CreatePaymentResponse
from openapi_server.models.get_payment_response import GetPaymentResponse
from openapi_server.models.list_payments_response import ListPaymentsResponse
from openapi_server.models.update_payment_request import UpdatePaymentRequest
from openapi_server.models.update_payment_response import UpdatePaymentResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_payment(client):
    """Test case for cancel_payment

    CancelPayment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/payments/{payment_id}/cancel'.format(payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_payment_by_idempotency_key(client):
    """Test case for cancel_payment_by_idempotency_key

    CancelPaymentByIdempotencyKey
    """
    body = {"request_body":{"idempotency_key":"a7e36d40-d24b-11e8-b568-0800200c9a66"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/payments/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_payment(client):
    """Test case for complete_payment

    CompletePayment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/payments/{payment_id}/complete'.format(payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_payment(client):
    """Test case for create_payment

    CreatePayment
    """
    body = {"request_body":{"amount_money":{"amount":200,"currency":"USD"},"app_fee_money":{"amount":10,"currency":"USD"},"autocomplete":True,"customer_id":"VDKXEEKPJN48QDG3BGGFAK05P8","idempotency_key":"4935a656-a929-4792-b97c-8848be85c27c","location_id":"XK3DBG77NJBFX","note":"Brief description","reference_id":"123456","source_id":"ccof:uIbfJXhXETSP197M3GB"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/payments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment(client):
    """Test case for get_payment

    GetPayment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/payments/{payment_id}'.format(payment_id='payment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment(client):
    """Test case for update_payment

    UpdatePayment
    """
    body = {"request_body":{"idempotency_key":"3d3c3b22-9572-4fc6-1111-e4d2f41b4122","payment":{"amount_money":{"amount":1000,"currency":"USD"},"tip_money":{"amount":300,"currency":"USD"},"version_token":"Z3okDzm2VRv5m5nE3WGx381ItTNhvjkB4VapByyz54h6o"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/payments/{payment_id}'.format(payment_id='payment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_payments_get(client):
    """Test case for v2_payments_get

    ListPayments
    """
    params = [('begin_time', 'begin_time_example'),
                    ('end_time', 'end_time_example'),
                    ('sort_order', 'sort_order_example'),
                    ('cursor', 'cursor_example'),
                    ('location_id', 'location_id_example'),
                    ('total', 56),
                    ('last_4', 'last_4_example'),
                    ('card_brand', 'card_brand_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

