# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_endpoint_policy_definition import ServiceEndpointPolicyDefinition


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policy_definitions_create_or_update(client):
    """Test case for service_endpoint_policy_definitions_create_or_update

    
    """
    service_endpoint_policy_definitions = {"name":"name","etag":"etag","properties":{"service":"service","serviceResources":["serviceResources","serviceResources"],"description":"description","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}/serviceEndpointPolicyDefinitions/{service_endpoint_policy_definition_name}'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', service_endpoint_policy_definition_name='service_endpoint_policy_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=service_endpoint_policy_definitions,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policy_definitions_get(client):
    """Test case for service_endpoint_policy_definitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}/serviceEndpointPolicyDefinitions/{service_endpoint_policy_definition_name}'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', service_endpoint_policy_definition_name='service_endpoint_policy_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

