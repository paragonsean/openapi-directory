# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_holder_notification_request import AccountHolderNotificationRequest
from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_account_holder_created(client):
    """Test case for post_balance_platform_account_holder_created

    Account holder created
    """
    account_holder_notification_request = openapi_server.AccountHolderNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.accountHolder.created',
        headers=headers,
        json=account_holder_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_account_holder_updated(client):
    """Test case for post_balance_platform_account_holder_updated

    Account holder updated
    """
    account_holder_notification_request = openapi_server.AccountHolderNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.accountHolder.updated',
        headers=headers,
        json=account_holder_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

