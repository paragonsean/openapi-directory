# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.customization_policies_list_response import CustomizationPoliciesListResponse
from openapi_server.models.customization_policy import CustomizationPolicy


pytestmark = pytest.mark.asyncio

async def test_customization_policies_get(client):
    """Test case for customization_policies_get

    Implements get of customization policy
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/customizationPolicies/{customization_policy_name}'.format(subscription_id='subscription_id_example', region_id='region_id_example', pc_name='pc_name_example', customization_policy_name='customization_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customization_policies_list(client):
    """Test case for customization_policies_list

    Implements get of customization policies list
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/customizationPolicies'.format(subscription_id='subscription_id_example', region_id='region_id_example', pc_name='pc_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

