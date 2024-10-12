# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_webhooks_payload_template_request import CreateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.get_network_webhooks_payload_templates200_response_inner import GetNetworkWebhooksPayloadTemplates200ResponseInner
from openapi_server.models.update_network_webhooks_payload_template_request import UpdateNetworkWebhooksPayloadTemplateRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_payload_template_2(client):
    """Test case for create_network_webhooks_payload_template_2

    Create a webhook payload template for a network
    """
    body = openapi_server.CreateNetworkWebhooksPayloadTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_webhooks_payload_template_2(client):
    """Test case for delete_network_webhooks_payload_template_2

    Destroy a webhook payload template for a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}'.format(network_id='network_id_example', payload_template_id='payload_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_payload_template_2(client):
    """Test case for get_network_webhooks_payload_template_2

    Get the webhook payload template for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}'.format(network_id='network_id_example', payload_template_id='payload_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_payload_templates_2(client):
    """Test case for get_network_webhooks_payload_templates_2

    List the webhook payload templates for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_webhooks_payload_template_2(client):
    """Test case for update_network_webhooks_payload_template_2

    Update a webhook payload template for a network
    """
    body = openapi_server.UpdateNetworkWebhooksPayloadTemplateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/webhooks/payloadTemplates/{payload_template_id}'.format(network_id='network_id_example', payload_template_id='payload_template_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

