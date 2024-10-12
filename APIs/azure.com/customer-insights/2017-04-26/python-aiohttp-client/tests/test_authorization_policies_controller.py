# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorization_policy import AuthorizationPolicy
from openapi_server.models.authorization_policy_list_result import AuthorizationPolicyListResult
from openapi_server.models.authorization_policy_resource_format import AuthorizationPolicyResourceFormat


pytestmark = pytest.mark.asyncio

async def test_authorization_policies_create_or_update(client):
    """Test case for authorization_policies_create_or_update

    
    """
    parameters = {"properties":{"secondaryKey":"secondaryKey","policyName":"policyName","permissions":["Read","Read"],"primaryKey":"primaryKey"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/authorizationPolicies/{authorization_policy_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', authorization_policy_name='authorization_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_policies_get(client):
    """Test case for authorization_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/authorizationPolicies/{authorization_policy_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', authorization_policy_name='authorization_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_policies_list_by_hub(client):
    """Test case for authorization_policies_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/authorizationPolicies'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_policies_regenerate_primary_key(client):
    """Test case for authorization_policies_regenerate_primary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/authorizationPolicies/{authorization_policy_name}/regeneratePrimaryKey'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', authorization_policy_name='authorization_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_policies_regenerate_secondary_key(client):
    """Test case for authorization_policies_regenerate_secondary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/authorizationPolicies/{authorization_policy_name}/regenerateSecondaryKey'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', authorization_policy_name='authorization_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

