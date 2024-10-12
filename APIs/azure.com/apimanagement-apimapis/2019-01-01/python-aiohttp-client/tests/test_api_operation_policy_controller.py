# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.api_operation_policy_get200_response import ApiOperationPolicyGet200Response
from openapi_server.models.api_operation_policy_list_by_operation200_response import ApiOperationPolicyListByOperation200Response


pytestmark = pytest.mark.asyncio

async def test_api_operation_policy_create_or_update(client):
    """Test case for api_operation_policy_create_or_update

    
    """
    parameters = openapi_server.ApiOperationPolicyGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_operation_policy_delete(client):
    """Test case for api_operation_policy_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_operation_policy_get(client):
    """Test case for api_operation_policy_get

    
    """
    params = [('format', xml),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_operation_policy_get_entity_tag(client):
    """Test case for api_operation_policy_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policies/{policy_id}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', policy_id='policy_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_operation_policy_list_by_operation(client):
    """Test case for api_operation_policy_list_by_operation

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/operations/{operation_id}/policies'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

