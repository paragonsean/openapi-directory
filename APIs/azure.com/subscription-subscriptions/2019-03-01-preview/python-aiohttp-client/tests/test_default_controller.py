# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.canceled_subscription_id import CanceledSubscriptionId
from openapi_server.models.enabled_subscription_id import EnabledSubscriptionId
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.renamed_subscription_id import RenamedSubscriptionId
from openapi_server.models.subscription_name import SubscriptionName


pytestmark = pytest.mark.asyncio

async def test_subscriptions_cancel(client):
    """Test case for subscriptions_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscription/cancel'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_enable(client):
    """Test case for subscriptions_enable

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscription/enable'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_rename(client):
    """Test case for subscriptions_rename

    
    """
    body = {"subscriptionName":"subscriptionName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscription/rename'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

