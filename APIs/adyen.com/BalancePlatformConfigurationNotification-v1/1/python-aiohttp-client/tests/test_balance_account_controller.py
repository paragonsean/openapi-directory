# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_account_notification_request import BalanceAccountNotificationRequest
from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.sweep_configuration_notification_request import SweepConfigurationNotificationRequest


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_balance_account_created(client):
    """Test case for post_balance_platform_balance_account_created

    Balance account created
    """
    balance_account_notification_request = openapi_server.BalanceAccountNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.balanceAccount.created',
        headers=headers,
        json=balance_account_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_balance_account_sweep_created(client):
    """Test case for post_balance_platform_balance_account_sweep_created

    Sweep created
    """
    sweep_configuration_notification_request = openapi_server.SweepConfigurationNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.balanceAccountSweep.created',
        headers=headers,
        json=sweep_configuration_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_balance_account_sweep_deleted(client):
    """Test case for post_balance_platform_balance_account_sweep_deleted

    Sweep deleted
    """
    sweep_configuration_notification_request = openapi_server.SweepConfigurationNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.balanceAccountSweep.deleted',
        headers=headers,
        json=sweep_configuration_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_balance_account_sweep_updated(client):
    """Test case for post_balance_platform_balance_account_sweep_updated

    Sweep updated
    """
    sweep_configuration_notification_request = openapi_server.SweepConfigurationNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.balanceAccountSweep.updated',
        headers=headers,
        json=sweep_configuration_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_balance_account_updated(client):
    """Test case for post_balance_platform_balance_account_updated

    Balance account updated
    """
    balance_account_notification_request = openapi_server.BalanceAccountNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.balanceAccount.updated',
        headers=headers,
        json=balance_account_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

