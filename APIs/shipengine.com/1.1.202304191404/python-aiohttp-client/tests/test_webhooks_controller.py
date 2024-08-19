# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_webhook_request_body import CreateWebhookRequestBody
from openapi_server.models.create_webhook_response_body import CreateWebhookResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_webhook_by_id_response_body import GetWebhookByIdResponseBody
from openapi_server.models.update_webhook_request_body import UpdateWebhookRequestBody
from openapi_server.models.webhook import Webhook


pytestmark = pytest.mark.asyncio

async def test_create_webhook(client):
    """Test case for create_webhook

    Create a Webhook
    """
    body = openapi_server.CreateWebhookRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/environment/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_webhook(client):
    """Test case for delete_webhook

    Delete Webhook By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/environment/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_by_id(client):
    """Test case for get_webhook_by_id

    Get Webhook By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/environment/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_webhooks(client):
    """Test case for list_webhooks

    List Webhooks
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/environment/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhook(client):
    """Test case for update_webhook

    Update a Webhook
    """
    body = openapi_server.UpdateWebhookRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/environment/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

