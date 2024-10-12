# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.ddos_custom_policies_update_tags_request import DdosCustomPoliciesUpdateTagsRequest
from openapi_server.models.ddos_custom_policy import DdosCustomPolicy


pytestmark = pytest.mark.asyncio

async def test_ddos_custom_policies_create_or_update(client):
    """Test case for ddos_custom_policies_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"resourceGuid":"resourceGuid","protocolCustomSettings":[{"protocol":"Tcp","sourceRateOverride":"sourceRateOverride","triggerRateOverride":"triggerRateOverride","triggerSensitivityOverride":"Relaxed"},{"protocol":"Tcp","sourceRateOverride":"sourceRateOverride","triggerRateOverride":"triggerRateOverride","triggerSensitivityOverride":"Relaxed"}],"publicIPAddresses":[{"id":"id"},{"id":"id"}],"provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ddosCustomPolicies/{ddos_custom_policy_name}'.format(resource_group_name='resource_group_name_example', ddos_custom_policy_name='ddos_custom_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ddos_custom_policies_delete(client):
    """Test case for ddos_custom_policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ddosCustomPolicies/{ddos_custom_policy_name}'.format(resource_group_name='resource_group_name_example', ddos_custom_policy_name='ddos_custom_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ddos_custom_policies_get(client):
    """Test case for ddos_custom_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ddosCustomPolicies/{ddos_custom_policy_name}'.format(resource_group_name='resource_group_name_example', ddos_custom_policy_name='ddos_custom_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ddos_custom_policies_update_tags(client):
    """Test case for ddos_custom_policies_update_tags

    
    """
    parameters = openapi_server.DdosCustomPoliciesUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/ddosCustomPolicies/{ddos_custom_policy_name}'.format(resource_group_name='resource_group_name_example', ddos_custom_policy_name='ddos_custom_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

