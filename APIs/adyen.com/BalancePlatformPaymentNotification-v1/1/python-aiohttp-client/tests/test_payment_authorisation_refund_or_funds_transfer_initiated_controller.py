# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.payment_notification_request import PaymentNotificationRequest


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_payment_created(client):
    """Test case for post_balance_platform_payment_created

    Payment authorisation, refund, or funds transfer initiated
    """
    payment_notification_request = openapi_server.PaymentNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.payment.created',
        headers=headers,
        json=payment_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_payment_updated(client):
    """Test case for post_balance_platform_payment_updated

    Payment authorisation expired or cancelled
    """
    payment_notification_request = openapi_server.PaymentNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.payment.updated',
        headers=headers,
        json=payment_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

