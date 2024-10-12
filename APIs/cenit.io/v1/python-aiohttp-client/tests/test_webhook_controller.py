# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.webhook import Webhook


pytestmark = pytest.mark.asyncio

async def test_setup_webhook_get(client):
    """Test case for setup_webhook_get

    Returns a list of webhooks
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/webhook/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_webhook_id_delete(client):
    """Test case for setup_webhook_id_delete

    Delete a webhook
    """
    headers = { 
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/setup/webhook/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_webhook_id_get(client):
    """Test case for setup_webhook_id_get

    Retrieve an existing webhook
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/webhook/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_webhook_post(client):
    """Test case for setup_webhook_post

    Create or update a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/setup/webhook/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

