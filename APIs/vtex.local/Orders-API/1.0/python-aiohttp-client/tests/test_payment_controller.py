# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_paymenttransaction import GetPaymenttransaction


pytestmark = pytest.mark.asyncio

async def test_get_paymenttransaction(client):
    """Test case for get_paymenttransaction

    Retrieve payment transaction
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/pvt/orders/{order_id}/payment-transaction'.format(order_id='1172452900788-01'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_payment_notification(client):
    """Test case for send_payment_notification

    Send payment notification
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/oms/pvt/orders/{order_id}/payments/{payment_id}/payment-notification'.format(order_id='1172452900788-01', payment_id='F5C1A4E20D3B4E07B7E871F5B5BC9F91'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

