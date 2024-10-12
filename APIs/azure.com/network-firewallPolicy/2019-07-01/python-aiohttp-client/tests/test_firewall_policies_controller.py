# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.firewall_policies_update_tags_default_response import FirewallPoliciesUpdateTagsDefaultResponse
from openapi_server.models.firewall_policies_update_tags_request import FirewallPoliciesUpdateTagsRequest
from openapi_server.models.firewall_policy import FirewallPolicy
from openapi_server.models.firewall_policy_list_result import FirewallPolicyListResult


pytestmark = pytest.mark.asyncio

async def test_firewall_policies_create_or_update(client):
    """Test case for firewall_policies_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"childPolicies":[{"id":"id"},{"id":"id"}],"ruleGroups":[{"id":"id"},{"id":"id"}],"threatIntelMode":"Alert","basePolicy":{"id":"id"},"firewalls":[{"id":"id"},{"id":"id"}],"provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}'.format(resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policies_delete(client):
    """Test case for firewall_policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}'.format(resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policies_get(client):
    """Test case for firewall_policies_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}'.format(resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policies_list(client):
    """Test case for firewall_policies_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policies_list_all(client):
    """Test case for firewall_policies_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/firewallPolicies'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewall_policies_update_tags(client):
    """Test case for firewall_policies_update_tags

    
    """
    firewall_policy_parameters = openapi_server.FirewallPoliciesUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/firewallPolicies/{firewall_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', firewall_policy_name='firewall_policy_name_example'),
        headers=headers,
        json=firewall_policy_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

