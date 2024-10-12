# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apis_list_by_service_default_response import ApisListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/vnd.ms-azure-apim.policy+xml not supported by Connexion")
async def test_api_operations_policy_create_or_update(client):
    """Test case for api_operations_policy_create_or_update

    
    """
    parameters = None
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/vnd.ms-azure-apim.policy+xml',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policy'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_operations_policy_delete(client):
    """Test case for api_operations_policy_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policy'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_operations_policy_get(client):
    """Test case for api_operations_policy_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/vnd.ms-azure-apim.policy+xml',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policy'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

