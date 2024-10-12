# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_a_webhook_request import CreateAWebhookRequest


pytestmark = pytest.mark.asyncio

async def test_create_a_webhook(client):
    """Test case for create_a_webhook

    Create a webhook
    """
    body = openapi_server.CreateAWebhookRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/webhooks'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_a_webhook(client):
    """Test case for delete_a_webhook

    Delete a webhook
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}/webhooks/{webhook_id}'.format(org_id='org_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_webhooks(client):
    """Test case for list_webhooks

    List webhooks
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/webhooks'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ping_a_webhook(client):
    """Test case for ping_a_webhook

    Ping a webhook
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/webhooks/{webhook_id}/ping'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', webhook_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_webhook(client):
    """Test case for retrieve_a_webhook

    Retrieve a webhook
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/webhooks/{webhook_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', webhook_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

