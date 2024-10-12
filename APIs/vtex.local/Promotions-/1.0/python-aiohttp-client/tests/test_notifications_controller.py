# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usagenotification_request import UsagenotificationRequest


pytestmark = pytest.mark.asyncio

async def test_usagenotification(client):
    """Test case for usagenotification

    Usage notification
    """
    body = {"accountId":"ffffffff-gggg-hhhh-iiii-jjjjjjjjjjjj","calculatorIds":["discount_basetestqa_1"],"coupon":"cupom","itemsCount":4,"orderId":"vbbbbbb-1","profileId":"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee","used":True}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pub/notifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

