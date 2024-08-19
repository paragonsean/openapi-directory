# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_request163_wrapper import NotificationRequest163Wrapper
from openapi_server.models.notification_response166_wrapper import NotificationResponse166Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/xml not supported by Connexion")
async def test_send_notification_refund_retry(client):
    """Test case for send_notification_refund_retry

    Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 
    """
    notification_request = openapi_server.NotificationRequest163Wrapper()
    headers = { 
        'Accept': 'N/A',
        'Content-Type': 'application/xml',
    }
    response = await client.request(
        method='POST',
        path='/send/v1/partners/{partner_id}/events/generate/refund'.format(partner_id='partner_id_example'),
        headers=headers,
        json=notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

