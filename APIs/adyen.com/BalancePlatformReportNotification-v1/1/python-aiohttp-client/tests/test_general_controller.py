# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.report_notification_request import ReportNotificationRequest


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_report_created(client):
    """Test case for post_balance_platform_report_created

    Report generated
    """
    report_notification_request = openapi_server.ReportNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.report.created',
        headers=headers,
        json=report_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

