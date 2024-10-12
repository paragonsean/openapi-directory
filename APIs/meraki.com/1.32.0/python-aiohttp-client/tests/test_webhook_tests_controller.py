# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_webhooks_webhook_test201_response import CreateNetworkWebhooksWebhookTest201Response
from openapi_server.models.create_network_webhooks_webhook_test_request import CreateNetworkWebhooksWebhookTestRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_webhook_test_2(client):
    """Test case for create_network_webhooks_webhook_test_2

    Send a test webhook for a network
    """
    body = openapi_server.CreateNetworkWebhooksWebhookTestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/webhooks/webhookTests'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_webhook_test_2(client):
    """Test case for get_network_webhooks_webhook_test_2

    Return the status of a webhook test for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/webhookTests/{webhook_test_id}'.format(network_id='network_id_example', webhook_test_id='webhook_test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

