# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_endpoint_policy_list_result import ServiceEndpointPolicyListResult


pytestmark = pytest.mark.asyncio

async def test_service_endpoint_policies_list_by_resource_group(client):
    """Test case for service_endpoint_policies_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/serviceEndpointPolicies'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

