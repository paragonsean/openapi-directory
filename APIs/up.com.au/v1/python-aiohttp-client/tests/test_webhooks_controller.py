# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.create_webhook_response import CreateWebhookResponse
from openapi_server.models.get_webhook_response import GetWebhookResponse
from openapi_server.models.list_webhook_delivery_logs_response import ListWebhookDeliveryLogsResponse
from openapi_server.models.list_webhooks_response import ListWebhooksResponse
from openapi_server.models.webhook_event_callback import WebhookEventCallback


pytestmark = pytest.mark.asyncio

async def test_webhooks_get(client):
    """Test case for webhooks_get

    List webhooks
    """
    params = [('page[size]', 30)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_id_delete(client):
    """Test case for webhooks_id_delete

    Delete webhook
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/webhooks/{id}'.format(id='a940825b-80b6-4798-b378-c6284259b4c5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_id_get(client):
    """Test case for webhooks_id_get

    Retrieve webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhooks/{id}'.format(id='c8283a72-24b0-4fd8-9b13-fccccab371e5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_post(client):
    """Test case for webhooks_post

    Create webhook
    """
    body = {"data":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_webhook_id_logs_get(client):
    """Test case for webhooks_webhook_id_logs_get

    List webhook logs
    """
    params = [('page[size]', 30)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhooks/{webhook_id}/logs'.format(webhook_id='7104f5df-4993-495f-9d29-2b4d062c03a9'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_webhook_id_ping_post(client):
    """Test case for webhooks_webhook_id_ping_post

    Ping webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/webhooks/{webhook_id}/ping'.format(webhook_id='830e127d-fb89-4400-92bb-f3f48289dcba'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

