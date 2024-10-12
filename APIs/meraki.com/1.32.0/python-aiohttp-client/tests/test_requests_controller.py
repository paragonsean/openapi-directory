# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_pii_request_request import CreateNetworkPiiRequestRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_pii_request_2(client):
    """Test case for create_network_pii_request_2

    Submit a new delete or restrict processing PII request
    """
    body = openapi_server.CreateNetworkPiiRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/pii/requests'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_pii_request_2(client):
    """Test case for delete_network_pii_request_2

    Delete a restrict processing PII request
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/pii/requests/{request_id}'.format(network_id='network_id_example', request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_request_2(client):
    """Test case for get_network_pii_request_2

    Return a PII request
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/requests/{request_id}'.format(network_id='network_id_example', request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_requests_2(client):
    """Test case for get_network_pii_requests_2

    List the PII requests for this network or organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/requests'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

