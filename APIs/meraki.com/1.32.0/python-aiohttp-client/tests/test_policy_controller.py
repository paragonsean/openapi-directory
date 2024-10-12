# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_client_policy_request import UpdateNetworkClientPolicyRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_client_policy_2(client):
    """Test case for get_network_client_policy_2

    Return the policy assigned to a client on the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/{client_id}/policy'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_client_policy_2(client):
    """Test case for update_network_client_policy_2

    Update the policy assigned to a client on the network
    """
    body = openapi_server.UpdateNetworkClientPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/clients/{client_id}/policy'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

