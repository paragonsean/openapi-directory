# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.not_found import NotFound
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhooks_create_payload import WebhooksCreatePayload
from openapi_server.models.webhooks_list_response import WebhooksListResponse


pytestmark = pytest.mark.asyncio

async def test_d_elete_webhook(client):
    """Test case for d_elete_webhook

    Delete a Webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_webhook(client):
    """Test case for g_et_webhook

    Show Webhook details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhooks/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_l_ist_webhooks(client):
    """Test case for l_ist_webhooks

    List all webhooks
    """
    params = [('events', 'video.encoding.quality.completed'),
                    ('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_webhooks(client):
    """Test case for p_ost_webhooks

    Create Webhook
    """
    body = openapi_server.WebhooksCreatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

