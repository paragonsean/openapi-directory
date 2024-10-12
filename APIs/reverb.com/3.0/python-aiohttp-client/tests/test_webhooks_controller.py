# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.webhooks_registrations_post_request import WebhooksRegistrationsPostRequest


pytestmark = pytest.mark.asyncio

async def test_webhooks_registrations_get(client):
    """Test case for webhooks_registrations_get

    Get webhook registrations
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/webhooks/registrations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_registrations_id_delete(client):
    """Test case for webhooks_registrations_id_delete

    Remove a webhook
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/webhooks/registrations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_registrations_id_get(client):
    """Test case for webhooks_registrations_id_get

    Get details of a webhook registration
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/webhooks/registrations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_registrations_post(client):
    """Test case for webhooks_registrations_post

    Register a webhook
    """
    body = openapi_server.WebhooksRegistrationsPostRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/webhooks/registrations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

