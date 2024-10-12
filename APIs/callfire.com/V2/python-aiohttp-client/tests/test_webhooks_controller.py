# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.item_list_webhook_resource import ItemListWebhookResource
from openapi_server.models.resource_id import ResourceId
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_page import WebhookPage
from openapi_server.models.webhook_resource import WebhookResource


pytestmark = pytest.mark.asyncio

async def test_create_webhook(client):
    """Test case for create_webhook

    Create a webhook
    """
    body = {"resource":"resource","secret":"secret","enabled":True,"expiresAt":5,"createdAt":5,"singleUse":True,"nonStrictSsl":True,"name":"name","callback":"callback","id":2,"fields":"fields","events":["events","events"],"updatedAt":7}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_webhook(client):
    """Test case for delete_webhook

    Delete a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/webhooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_webhook_resources(client):
    """Test case for find_webhook_resources

    Find webhook resources
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/webhooks/resources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_webhooks(client):
    """Test case for find_webhooks

    Find webhooks
    """
    params = [('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0),
                    ('name', 'name_example'),
                    ('resource', 'resource_example'),
                    ('event', 'event_example'),
                    ('callback', 'param_callback_example'),
                    ('enabled', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook(client):
    """Test case for get_webhook

    Find a specific webhook
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/webhooks/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_resource(client):
    """Test case for get_webhook_resource

    Find specific webhook resource
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/webhooks/resources/{resource}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhook(client):
    """Test case for update_webhook

    Update a webhook
    """
    body = {"resource":"resource","secret":"secret","enabled":True,"expiresAt":5,"createdAt":5,"singleUse":True,"nonStrictSsl":True,"name":"name","callback":"callback","id":2,"fields":"fields","events":["events","events"],"updatedAt":7}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/webhooks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

