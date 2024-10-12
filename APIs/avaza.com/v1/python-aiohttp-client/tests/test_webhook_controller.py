# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_subscription import CreateSubscription
from openapi_server.models.subscribe_result import SubscribeResult
from openapi_server.models.webhook_list import WebhookList


pytestmark = pytest.mark.asyncio

async def test_webhook_delete(client):
    """Test case for webhook_delete

    Delete Webhook Subscription by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Webhook/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_delete_by_url(client):
    """Test case for webhook_delete_by_url

    Delete webhook subscription by URL
    """
    params = [('target_url', 'target_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Webhook',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_get(client):
    """Test case for webhook_get

    Get list of Webhook Subscriptions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Webhook',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_get_by_id(client):
    """Test case for webhook_get_by_id

    Get Webhook Subscription by SubscriptionID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Webhook/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_webhook_post(client):
    """Test case for webhook_post

    Subscribe to Webhook. On success, returns ID of webhook subscription.
    """
    model = {"target_url":"target_url","secret":"secret","event":"event"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Webhook',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

