# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.card_order_notification_request import CardOrderNotificationRequest


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_cardorder_created(client):
    """Test case for post_balance_platform_cardorder_created

    Card order created
    """
    card_order_notification_request = openapi_server.CardOrderNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.cardorder.created',
        headers=headers,
        json=card_order_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_cardorder_updated(client):
    """Test case for post_balance_platform_cardorder_updated

    Card order updated
    """
    card_order_notification_request = openapi_server.CardOrderNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.cardorder.updated',
        headers=headers,
        json=card_order_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

