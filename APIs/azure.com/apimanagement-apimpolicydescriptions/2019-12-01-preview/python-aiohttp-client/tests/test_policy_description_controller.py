# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.policy_description_list_by_service200_response import PolicyDescriptionListByService200Response
from openapi_server.models.policy_description_list_by_service_default_response import PolicyDescriptionListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_policy_description_list_by_service(client):
    """Test case for policy_description_list_by_service

    
    """
    params = [('scope', 'scope_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/policyDescriptions'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

