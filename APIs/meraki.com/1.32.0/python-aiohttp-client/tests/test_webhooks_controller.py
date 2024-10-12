# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_webhooks_http_server_request import CreateNetworkWebhooksHttpServerRequest
from openapi_server.models.create_network_webhooks_payload_template_request import CreateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.create_network_webhooks_webhook_test201_response import CreateNetworkWebhooksWebhookTest201Response
from openapi_server.models.create_network_webhooks_webhook_test_request import CreateNetworkWebhooksWebhookTestRequest
from openapi_server.models.get_network_webhooks_http_servers200_response_inner import GetNetworkWebhooksHttpServers200ResponseInner
from openapi_server.models.get_network_webhooks_payload_templates200_response_inner import GetNetworkWebhooksPayloadTemplates200ResponseInner
from openapi_server.models.get_organization_webhooks_logs200_response_inner import GetOrganizationWebhooksLogs200ResponseInner
from openapi_server.models.update_network_webhooks_http_server_request import UpdateNetworkWebhooksHttpServerRequest
from openapi_server.models.update_network_webhooks_payload_template_request import UpdateNetworkWebhooksPayloadTemplateRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_http_server_1(client):
    """Test case for create_network_webhooks_http_server_1

    Add an HTTP server to a network
    """
    body = openapi_server.CreateNetworkWebhooksHttpServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/webhooks/httpServers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_payload_template_1(client):
    """Test case for create_network_webhooks_payload_template_1

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

async def test_create_network_webhooks_webhook_test_1(client):
    """Test case for create_network_webhooks_webhook_test_1

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

async def test_delete_network_webhooks_http_server_1(client):
    """Test case for delete_network_webhooks_http_server_1

    Delete an HTTP server from a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/webhooks/httpServers/{http_server_id}'.format(network_id='network_id_example', http_server_id='http_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_webhooks_payload_template_1(client):
    """Test case for delete_network_webhooks_payload_template_1

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

async def test_get_network_webhooks_http_server_1(client):
    """Test case for get_network_webhooks_http_server_1

    Return an HTTP server for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/httpServers/{http_server_id}'.format(network_id='network_id_example', http_server_id='http_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_http_servers_1(client):
    """Test case for get_network_webhooks_http_servers_1

    List the HTTP servers for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/webhooks/httpServers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_webhooks_payload_template_1(client):
    """Test case for get_network_webhooks_payload_template_1

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

async def test_get_network_webhooks_payload_templates_1(client):
    """Test case for get_network_webhooks_payload_templates_1

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

async def test_get_network_webhooks_webhook_test_1(client):
    """Test case for get_network_webhooks_webhook_test_1

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


pytestmark = pytest.mark.asyncio

async def test_get_organization_webhooks_alert_types_1(client):
    """Test case for get_organization_webhooks_alert_types_1

    Return a list of alert types to be used with managing webhook alerts
    """
    params = [('productType', 'product_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/webhooks/alertTypes'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_webhooks_logs_1(client):
    """Test case for get_organization_webhooks_logs_1

    Return the log of webhook POSTs sent
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/webhooks/logs'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_webhooks_http_server_1(client):
    """Test case for update_network_webhooks_http_server_1

    Update an HTTP server
    """
    body = openapi_server.UpdateNetworkWebhooksHttpServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/webhooks/httpServers/{http_server_id}'.format(network_id='network_id_example', http_server_id='http_server_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_webhooks_payload_template_1(client):
    """Test case for update_network_webhooks_payload_template_1

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

