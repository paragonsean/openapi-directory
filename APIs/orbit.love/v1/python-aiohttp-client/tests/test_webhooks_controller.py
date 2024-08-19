# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.webhook_subscription import WebhookSubscription


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_webhooks_get(client):
    """Test case for workspace_slug_webhooks_get

    List webhooks in a workspace
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/webhooks'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_webhooks_id_delete(client):
    """Test case for workspace_slug_webhooks_id_delete

    Delete a webhook
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/{workspace_slug}/webhooks/{id}'.format(workspace_slug='workspace_slug_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_webhooks_id_get(client):
    """Test case for workspace_slug_webhooks_id_get

    Get a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/webhooks/{id}'.format(workspace_slug='workspace_slug_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_webhooks_id_put(client):
    """Test case for workspace_slug_webhooks_id_put

    Update a webhook
    """
    body = openapi_server.WebhookSubscription()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/{workspace_slug}/webhooks/{id}'.format(workspace_slug='workspace_slug_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_webhooks_post(client):
    """Test case for workspace_slug_webhooks_post

    Create a webhook
    """
    body = openapi_server.WebhookSubscription()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{workspace_slug}/webhooks'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

