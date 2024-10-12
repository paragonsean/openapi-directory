# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_group_policy_request import CreateNetworkGroupPolicyRequest
from openapi_server.models.update_network_group_policy_request import UpdateNetworkGroupPolicyRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_group_policy_1(client):
    """Test case for create_network_group_policy_1

    Create a group policy
    """
    body = openapi_server.CreateNetworkGroupPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/groupPolicies'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_group_policy_1(client):
    """Test case for delete_network_group_policy_1

    Delete a group policy
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/groupPolicies/{group_policy_id}'.format(network_id='network_id_example', group_policy_id='group_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_group_policies_1(client):
    """Test case for get_network_group_policies_1

    List the group policies in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/groupPolicies'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_group_policy_1(client):
    """Test case for get_network_group_policy_1

    Display a group policy
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/groupPolicies/{group_policy_id}'.format(network_id='network_id_example', group_policy_id='group_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_group_policy_1(client):
    """Test case for update_network_group_policy_1

    Update a group policy
    """
    body = openapi_server.UpdateNetworkGroupPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/groupPolicies/{group_policy_id}'.format(network_id='network_id_example', group_policy_id='group_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

