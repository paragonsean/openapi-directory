# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.webhook_base_info import WebhookBaseInfo
from openapi_server.models.webhook_info import WebhookInfo


pytestmark = pytest.mark.asyncio

async def test_get_webhook_by_id(client):
    """Test case for get_webhook_by_id

    Get Webhook by Id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_get(client):
    """Test case for webhooks_get

    Get Webhooks
    """
    params = [('teamId', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_webhooks_post(client):
    """Test case for webhooks_post

    Create Webhook
    """
    body = {"teamId":"teamId","name":"name","externalAddress":"externalAddress"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_webhook_id_delete(client):
    """Test case for webhooks_webhook_id_delete

    Delete Webhook by Id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_webhook_id_disable_post(client):
    """Test case for webhooks_webhook_id_disable_post

    Ability to enable a webHook.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/webhooks/{webhook_id}/disable'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_webhook_id_enable_post(client):
    """Test case for webhooks_webhook_id_enable_post

    Ability to disable a webHook.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/webhooks/{webhook_id}/enable'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_webhooks_webhook_id_put(client):
    """Test case for webhooks_webhook_id_put

    Update Webhook by Id
    """
    body = {"teamId":"teamId","name":"name","externalAddress":"externalAddress"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

