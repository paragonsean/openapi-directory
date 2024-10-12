# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_adaptive_policy_policy_request import CreateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.get_network_policies_by_client200_response_inner import GetNetworkPoliciesByClient200ResponseInner
from openapi_server.models.update_organization_adaptive_policy_policy_request import UpdateOrganizationAdaptivePolicyPolicyRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_adaptive_policy_policy_2(client):
    """Test case for create_organization_adaptive_policy_policy_2

    Add an Adaptive Policy
    """
    body = openapi_server.CreateOrganizationAdaptivePolicyPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_adaptive_policy_policy_2(client):
    """Test case for delete_organization_adaptive_policy_policy_2

    Delete an Adaptive Policy
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_policies_by_client_1(client):
    """Test case for get_network_policies_by_client_1

    Get policies for all clients with policies
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/policies/byClient'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_policies_2(client):
    """Test case for get_organization_adaptive_policy_policies_2

    List adaptive policies in an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_policy_2(client):
    """Test case for get_organization_adaptive_policy_policy_2

    Return an adaptive policy
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_policy_2(client):
    """Test case for update_organization_adaptive_policy_policy_2

    Update an Adaptive Policy
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicyPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/policies/{id}'.format(organization_id='organization_id_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

