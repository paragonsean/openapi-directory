# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_create import WebhookCreate


pytestmark = pytest.mark.asyncio

async def test_create_webhook(client):
    """Test case for create_webhook

    Create a new webhook subscription
    """
    body = {"signingKey":"signingKey","signingAlgo":"HMAC_SHA256","metadataPolicy":"NONE","events":["CALL"],"url":"https://www.example.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/t/vbc.prod/vis/v1/self/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_webhook(client):
    """Test case for destroy_webhook

    Remove a web hook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/t/vbc.prod/vis/v1/self/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_webhooks(client):
    """Test case for list_webhooks

    List web hooks
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_renew_webhook(client):
    """Test case for renew_webhook

    Renews a web hook
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/t/vbc.prod/vis/v1/self/webhooks/{id}/renew'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_view_webhook(client):
    """Test case for view_webhook

    Get web hook details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

