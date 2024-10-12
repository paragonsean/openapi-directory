# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_request159_wrapper import NotificationRequest159Wrapper
from openapi_server.models.notification_response162_wrapper import NotificationResponse162Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_send_notification_payment_retry(client):
    """Test case for send_notification_payment_retry

    Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 
    """
    notification_request = openapi_server.NotificationRequest159Wrapper()
    headers = { 
        'Accept': 'N/A',
        'Content-Type': 'application/xml',
    }
    response = await client.request(
        method='POST',
        path='/send/v1/partners/{partner_id}/events/generate/payment'.format(partner_id='partner_id_example'),
        headers=headers,
        json=notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

