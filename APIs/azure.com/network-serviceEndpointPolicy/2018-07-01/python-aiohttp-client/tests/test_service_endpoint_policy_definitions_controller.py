# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_endpoint_policy_definition_list_result import ServiceEndpointPolicyDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policy_definitions_delete(client):
    """Test case for service_endpoint_policy_definitions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}/serviceEndpointPolicyDefinitions/{service_endpoint_policy_definition_name}'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', service_endpoint_policy_definition_name='service_endpoint_policy_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policy_definitions_list_by_resource_group(client):
    """Test case for service_endpoint_policy_definitions_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies/{service_endpoint_policy_name}/serviceEndpointPolicyDefinitions'.format(resource_group_name='resource_group_name_example', service_endpoint_policy_name='service_endpoint_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

