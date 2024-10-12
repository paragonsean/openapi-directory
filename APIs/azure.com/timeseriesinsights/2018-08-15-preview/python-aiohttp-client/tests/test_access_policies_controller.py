# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_policy_create_or_update_parameters import AccessPolicyCreateOrUpdateParameters
from openapi_server.models.access_policy_list_response import AccessPolicyListResponse
from openapi_server.models.access_policy_resource import AccessPolicyResource
from openapi_server.models.access_policy_update_parameters import AccessPolicyUpdateParameters
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_access_policies_create_or_update(client):
    """Test case for access_policies_create_or_update

    
    """
    parameters = {"properties":{"principalObjectId":"principalObjectId","roles":["Reader","Reader"],"description":"description"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/accessPolicies/{access_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', access_policy_name='access_policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_access_policies_delete(client):
    """Test case for access_policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/accessPolicies/{access_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', access_policy_name='access_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_access_policies_get(client):
    """Test case for access_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/accessPolicies/{access_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', access_policy_name='access_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_access_policies_list_by_environment(client):
    """Test case for access_policies_list_by_environment

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/accessPolicies'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_access_policies_update(client):
    """Test case for access_policies_update

    
    """
    access_policy_update_parameters = {"properties":{"roles":["Reader","Reader"],"description":"description"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/accessPolicies/{access_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', access_policy_name='access_policy_name_example'),
        headers=headers,
        json=access_policy_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

