# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.jit_network_access_policies_list import JitNetworkAccessPoliciesList
from openapi_server.models.jit_network_access_policy import JitNetworkAccessPolicy
from openapi_server.models.jit_network_access_policy_initiate_request import JitNetworkAccessPolicyInitiateRequest
from openapi_server.models.jit_network_access_request import JitNetworkAccessRequest


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_create_or_update(client):
    """Test case for jit_network_access_policies_create_or_update

    
    """
    body = {"properties":{"provisioningState":"provisioningState","requests":[{"virtualMachines":[{"id":"id","ports":[{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"},{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"}]},{"id":"id","ports":[{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"},{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"}]}],"requestor":"requestor","startTimeUtc":"2000-01-23T04:56:07.000+00:00"},{"virtualMachines":[{"id":"id","ports":[{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"},{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"}]},{"id":"id","ports":[{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"},{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","statusReason":"Expired","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"allowedSourceAddressPrefix":"allowedSourceAddressPrefix","status":"Revoked"}]}],"requestor":"requestor","startTimeUtc":"2000-01-23T04:56:07.000+00:00"}],"virtualMachines":[{"id":"id","ports":[{"number":39500,"protocol":"TCP","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"maxRequestAccessDuration":"maxRequestAccessDuration","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"},{"number":39500,"protocol":"TCP","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"maxRequestAccessDuration":"maxRequestAccessDuration","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"}]},{"id":"id","ports":[{"number":39500,"protocol":"TCP","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"maxRequestAccessDuration":"maxRequestAccessDuration","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"},{"number":39500,"protocol":"TCP","allowedSourceAddressPrefixes":["allowedSourceAddressPrefixes","allowedSourceAddressPrefixes"],"maxRequestAccessDuration":"maxRequestAccessDuration","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"}]}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/jitNetworkAccessPolicies/{jit_network_access_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', asc_location='asc_location_example', jit_network_access_policy_name='jit_network_access_policy_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_delete(client):
    """Test case for jit_network_access_policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/jitNetworkAccessPolicies/{jit_network_access_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', asc_location='asc_location_example', jit_network_access_policy_name='jit_network_access_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_get(client):
    """Test case for jit_network_access_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/jitNetworkAccessPolicies/{jit_network_access_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', asc_location='asc_location_example', jit_network_access_policy_name='jit_network_access_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_initiate(client):
    """Test case for jit_network_access_policies_initiate

    
    """
    body = {"virtualMachines":[{"id":"id","ports":[{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"},{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"}]},{"id":"id","ports":[{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"},{"number":5248,"endTimeUtc":"2000-01-23T04:56:07.000+00:00","allowedSourceAddressPrefix":"allowedSourceAddressPrefix"}]}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/jitNetworkAccessPolicies/{jit_network_access_policy_name}/{jit_network_access_policy_initiate_type}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', asc_location='asc_location_example', jit_network_access_policy_name='jit_network_access_policy_name_example', jit_network_access_policy_initiate_type='jit_network_access_policy_initiate_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_list(client):
    """Test case for jit_network_access_policies_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/jitNetworkAccessPolicies'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_list_by_region(client):
    """Test case for jit_network_access_policies_list_by_region

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}/jitNetworkAccessPolicies'.format(subscription_id='subscription_id_example', asc_location='asc_location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_list_by_resource_group(client):
    """Test case for jit_network_access_policies_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/jitNetworkAccessPolicies'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jit_network_access_policies_list_by_resource_group_and_region(client):
    """Test case for jit_network_access_policies_list_by_resource_group_and_region

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/jitNetworkAccessPolicies'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', asc_location='asc_location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

