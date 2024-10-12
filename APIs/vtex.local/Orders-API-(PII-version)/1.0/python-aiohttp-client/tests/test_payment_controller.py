# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_send_payment_notification2(client):
    """Test case for send_payment_notification2

    Send payment notification
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/pvt/document/{order_id}/payment/{payment_id}/notify-payment'.format(order_id='70caf3941s6df1', payment_id='45hsfg5jkyu1384jdsfgh654sfgj1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

