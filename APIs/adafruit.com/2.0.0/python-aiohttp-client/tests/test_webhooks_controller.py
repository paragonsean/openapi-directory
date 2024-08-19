# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_webhook_feed_data_request import CreateWebhookFeedDataRequest
from openapi_server.models.data import Data


pytestmark = pytest.mark.asyncio

async def test_create_raw_webhook_feed_data(client):
    """Test case for create_raw_webhook_feed_data

    Send arbitrary data to a feed via webhook URL.
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/webhooks/feed/:token/raw',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_webhook_feed_data(client):
    """Test case for create_webhook_feed_data

    Send data to a feed via webhook URL.
    """
    payload = openapi_server.CreateWebhookFeedDataRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/webhooks/feed/:token',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

