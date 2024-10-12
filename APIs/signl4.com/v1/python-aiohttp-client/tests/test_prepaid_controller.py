# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.prepaid_balance_info import PrepaidBalanceInfo
from openapi_server.models.prepaid_settings_info import PrepaidSettingsInfo
from openapi_server.models.prepaid_transaction_info import PrepaidTransactionInfo


pytestmark = pytest.mark.asyncio

async def test_prepaid_balance_get(client):
    """Test case for prepaid_balance_get

    Get your subscription's current prepaid balance.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/prepaid/balance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prepaid_settings_get(client):
    """Test case for prepaid_settings_get

    Get your subscription's current prepaid settings.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/prepaid/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_prepaid_settings_put(client):
    """Test case for prepaid_settings_put

    Update your subscription's current prepaid settings.
    """
    body = {"topUpLimit":6,"topUpAmount":0,"topUpEnabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/prepaid/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prepaid_transactions_get(client):
    """Test case for prepaid_transactions_get

    Get your subscription's prepaid transactions.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/prepaid/transactions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_prepaid_balance_get(client):
    """Test case for subscriptions_subscription_id_prepaid_balance_get

    Get a subscription's current prepaid balance.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}/prepaidBalance'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_prepaid_settings_get(client):
    """Test case for subscriptions_subscription_id_prepaid_settings_get

    Get a subscription's current prepaid settings.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}/prepaidSettings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_subscriptions_subscription_id_prepaid_settings_put(client):
    """Test case for subscriptions_subscription_id_prepaid_settings_put

    Update a subscription's current prepaid settings.
    """
    body = {"topUpLimit":6,"topUpAmount":0,"topUpEnabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/subscriptions/{subscription_id}/prepaidSettings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_subscription_id_prepaid_transactions_get(client):
    """Test case for subscriptions_subscription_id_prepaid_transactions_get

    Get a subscription's prepaid transactions.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/subscriptions/{subscription_id}/prepaidTransactions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

