# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_endpoint_policies_update_request import ServiceEndpointPoliciesUpdateRequest
from openapi_server.models.service_endpoint_policy import ServiceEndpointPolicy
from openapi_server.models.service_endpoint_policy_list_result import ServiceEndpointPolicyListResult


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policies_create_or_update(client):
    """Test case for service_endpoint_policies_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"resourceGuid":"resourceGuid","provisioningState":"provisioningState","serviceEndpointPolicyDefinitions":[{"name":"name","etag":"etag","properties":{"service":"service","serviceResources":["serviceResources","serviceResources"],"description":"description","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"service":"service","serviceResources":["serviceResources","serviceResources"],"description":"description","provisioningState":"provisioningState"}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policies_delete(client):
    """Test case for service_endpoint_policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policies_get(client):
    """Test case for service_endpoint_policies_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policies_list(client):
    """Test case for service_endpoint_policies_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/ServiceEndpointPolicies'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policies_update(client):
    """Test case for service_endpoint_policies_update

    
    """
    parameters = openapi_server.ServiceEndpointPoliciesUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

