# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_response import NotificationResponse
from openapi_server.models.payment_failure_notification import PaymentFailureNotification
from openapi_server.models.report_available_notification import ReportAvailableNotification


pytestmark = pytest.mark.asyncio

async def test_post_paymentfailure(client):
    """Test case for post_paymentfailure

    Booking for a capture or refund failed
    """
    payment_failure_notification = openapi_server.PaymentFailureNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/PAYMENT_FAILURE',
        headers=headers,
        json=payment_failure_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_reportavailable(client):
    """Test case for post_reportavailable

    Report available
    """
    report_available_notification = openapi_server.ReportAvailableNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/REPORT_AVAILABLE',
        headers=headers,
        json=report_available_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

