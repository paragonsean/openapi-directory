# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_switch_access_policy_request import CreateNetworkSwitchAccessPolicyRequest
from openapi_server.models.get_network_switch_access_policies200_response_inner import GetNetworkSwitchAccessPolicies200ResponseInner
from openapi_server.models.update_network_switch_access_policy_request import UpdateNetworkSwitchAccessPolicyRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_access_policy_1(client):
    """Test case for create_network_switch_access_policy_1

    Create an access policy for a switch network
    """
    body = openapi_server.CreateNetworkSwitchAccessPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/accessPolicies'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_access_policy_1(client):
    """Test case for delete_network_switch_access_policy_1

    Delete an access policy for a switch network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/accessPolicies/{access_policy_number}'.format(network_id='network_id_example', access_policy_number='access_policy_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_access_policies_1(client):
    """Test case for get_network_switch_access_policies_1

    List the access policies for a switch network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/accessPolicies'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_access_policy_1(client):
    """Test case for get_network_switch_access_policy_1

    Return a specific access policy for a switch network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/accessPolicies/{access_policy_number}'.format(network_id='network_id_example', access_policy_number='access_policy_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_access_policy_1(client):
    """Test case for update_network_switch_access_policy_1

    Update an access policy for a switch network
    """
    body = openapi_server.UpdateNetworkSwitchAccessPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/accessPolicies/{access_policy_number}'.format(network_id='network_id_example', access_policy_number='access_policy_number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

