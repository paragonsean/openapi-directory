# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.webhook_response import WebhookResponse
from openapi_server.models.webhooks_response import WebhooksResponse
from openapi_server.models.webhooks_subscribe_request import WebhooksSubscribeRequest


pytestmark = pytest.mark.asyncio

async def test_webhooks_fetch_all(client):
    """Test case for webhooks_fetch_all

    Fetch active webhooks
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/webhooks'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_subscribe(client):
    """Test case for webhooks_subscribe

    Subscribe to message events
    """
    body = openapi_server.WebhooksSubscribeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/accounts/{account_id}/webhooks'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_unsubscribe(client):
    """Test case for webhooks_unsubscribe

    Unsubscribe to message events
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/accounts/{account_id}/webhooks/{url}'.format(account_id='account_id_example', url='url_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

