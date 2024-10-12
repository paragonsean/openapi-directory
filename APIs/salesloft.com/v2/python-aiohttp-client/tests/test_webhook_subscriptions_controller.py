# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription import Subscription


pytestmark = pytest.mark.asyncio

async def test_v2_webhook_subscriptions_get(client):
    """Test case for v2_webhook_subscriptions_get

    List webhook subscriptions
    """
    params = [('enabled', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/webhook_subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_webhook_subscriptions_id_delete(client):
    """Test case for v2_webhook_subscriptions_id_delete

    Delete a webhook subscription
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/webhook_subscriptions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_webhook_subscriptions_id_get(client):
    """Test case for v2_webhook_subscriptions_id_get

    Fetch a webhook subscription
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/webhook_subscriptions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_webhook_subscriptions_id_put(client):
    """Test case for v2_webhook_subscriptions_id_put

    Update a webhook subscription
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'enabled': True
        }
    response = await client.request(
        method='PUT',
        path='/v2/webhook_subscriptions/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_webhook_subscriptions_post(client):
    """Test case for v2_webhook_subscriptions_post

    Create a webhook subscription
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'callback_token': 'callback_token_example',
        'callback_url': 'callback_url_example',
        'event_type': 'event_type_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/webhook_subscriptions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

