# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.jit_request_definition import JitRequestDefinition
from openapi_server.models.jit_request_definition_list_result import JitRequestDefinitionListResult
from openapi_server.models.jit_request_patchable import JitRequestPatchable


pytestmark = pytest.mark.asyncio

async def test_jit_requests_create_or_update(client):
    """Test case for jit_requests_create_or_update

    
    """
    parameters = {"properties":{"jitSchedulingPolicy":{"duration":"duration","startTime":"2000-01-23T04:56:07.000+00:00","type":"NotSpecified"},"updatedBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"createdBy":{"puid":"puid","oid":"oid","applicationId":"applicationId"},"jitRequestState":"NotSpecified","jitAuthorizationPolicies":[{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"},{"roleDefinitionId":"roleDefinitionId","principalId":"principalId"}],"publisherTenantId":"publisherTenantId","provisioningState":"NotSpecified","applicationResourceId":"applicationResourceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/jitRequests/{jit_request_name}'.format(resource_group_name='resource_group_name_example', jit_request_name='jit_request_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_requests_delete(client):
    """Test case for jit_requests_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/jitRequests/{jit_request_name}'.format(resource_group_name='resource_group_name_example', jit_request_name='jit_request_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_requests_get(client):
    """Test case for jit_requests_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/jitRequests/{jit_request_name}'.format(resource_group_name='resource_group_name_example', jit_request_name='jit_request_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_requests_list_by_resource_group(client):
    """Test case for jit_requests_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/jitRequests'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_requests_list_by_subscription(client):
    """Test case for jit_requests_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Solutions/jitRequests'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_requests_update(client):
    """Test case for jit_requests_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/jitRequests/{jit_request_name}'.format(resource_group_name='resource_group_name_example', jit_request_name='jit_request_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

