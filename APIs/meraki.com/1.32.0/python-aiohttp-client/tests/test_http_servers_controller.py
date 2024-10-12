# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_webhooks_http_server_request import CreateNetworkWebhooksHttpServerRequest
from openapi_server.models.get_network_webhooks_http_servers200_response_inner import GetNetworkWebhooksHttpServers200ResponseInner
from openapi_server.models.update_network_webhooks_http_server_request import UpdateNetworkWebhooksHttpServerRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_webhooks_http_server_2(client):
    """Test case for create_network_webhooks_http_server_2

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

async def test_delete_network_webhooks_http_server_2(client):
    """Test case for delete_network_webhooks_http_server_2

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

async def test_get_network_webhooks_http_server_2(client):
    """Test case for get_network_webhooks_http_server_2

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

async def test_get_network_webhooks_http_servers_2(client):
    """Test case for get_network_webhooks_http_servers_2

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

async def test_update_network_webhooks_http_server_2(client):
    """Test case for update_network_webhooks_http_server_2

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

