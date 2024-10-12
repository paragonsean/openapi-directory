# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aspsps import Aspsps
from openapi_server.models.new_payment_request import NewPaymentRequest
from openapi_server.models.new_payment_request_response import NewPaymentRequestResponse
from openapi_server.models.payment_request import PaymentRequest


pytestmark = pytest.mark.asyncio

async def test_get_list_of_aspsps(client):
    """Test case for get_list_of_aspsps

    Get list of ASPSPs / Banks
    """
    params = [('currency', 'EUR')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/aspsps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_details(client):
    """Test case for get_payment_details

    Get Payment Details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/payments/{payment_uuid}'.format(payment_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_new_payment_request(client):
    """Test case for new_payment_request

    Create a Fire Open Payment request
    """
    body = openapi_server.NewPaymentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/paymentrequests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

