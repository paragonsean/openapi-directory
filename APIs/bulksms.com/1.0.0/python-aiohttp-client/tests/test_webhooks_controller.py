# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_entry import WebhookEntry


pytestmark = pytest.mark.asyncio

async def test_webhooks_get(client):
    """Test case for webhooks_get

    List webhooks
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_id_delete(client):
    """Test case for webhooks_id_delete

    Delete a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_id_get(client):
    """Test case for webhooks_id_get

    Read a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_id_post(client):
    """Test case for webhooks_id_post

    Update a webhook
    """
    body = {"contactEmailAddress":"tech_team@example.com","invokeOption":"MANY","name":"My MT Webhook","active":True,"triggerScope":"SENT","onWebApp":True,"url":"https://www.example.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_post(client):
    """Test case for webhooks_post

    Create a webhook
    """
    body = {"contactEmailAddress":"tech_team@example.com","invokeOption":"MANY","name":"My MT Webhook","active":True,"triggerScope":"SENT","onWebApp":True,"url":"https://www.example.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

