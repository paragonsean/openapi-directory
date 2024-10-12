# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.capture_payment_out import CapturePaymentOut
from openapi_server.models.create_payment_in import CreatePaymentIn
from openapi_server.models.create_payment_out import CreatePaymentOut
from openapi_server.models.list_payments_out import ListPaymentsOut


pytestmark = pytest.mark.asyncio

async def test_capture_payment(client):
    """Test case for capture_payment

    Capture payment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{key}/payments/capture'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_payment(client):
    """Test case for create_payment

    Register a payment
    """
    input = openapi_server.CreatePaymentIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{key}/payments'.format(key='key_example'),
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payments(client):
    """Test case for list_payments

    List payments
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transactions/{key}/payments'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

