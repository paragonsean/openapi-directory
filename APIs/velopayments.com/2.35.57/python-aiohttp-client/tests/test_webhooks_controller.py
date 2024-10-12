# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.ping_response import PingResponse
from openapi_server.models.update_webhook_request import UpdateWebhookRequest
from openapi_server.models.webhook_response import WebhookResponse
from openapi_server.models.webhooks_response import WebhooksResponse


pytestmark = pytest.mark.asyncio

async def test_create_webhook_v1(client):
    """Test case for create_webhook_v1

    Create Webhook
    """
    body = {"authorizationHeader":"authorizationHeader","categories":[null,null],"enabled":True,"payorId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","webhookUrl":"webhookUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_v1(client):
    """Test case for get_webhook_v1

    Get details about the given webhook.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_webhooks_v1(client):
    """Test case for list_webhooks_v1

    List the details about the webhooks for the given payor.
    """
    params = [('page', 1),
                    ('pageSize', 25),
                    ('payorId', 'payor_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ping_webhook_v1(client):
    """Test case for ping_webhook_v1

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/webhooks/{webhook_id}/ping'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhook_v1(client):
    """Test case for update_webhook_v1

    Update Webhook
    """
    body = {"authorizationHeader":"authorizationHeader","categories":[null,null],"enabled":True,"webhookUrl":"webhookUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

