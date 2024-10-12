# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.information_protection_policies_list_default_response import InformationProtectionPoliciesListDefaultResponse
from openapi_server.models.information_protection_policy import InformationProtectionPolicy
from openapi_server.models.information_protection_policy_list import InformationProtectionPolicyList


pytestmark = pytest.mark.asyncio

async def test_information_protection_policies_create_or_update(client):
    """Test case for information_protection_policies_create_or_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Security/informationProtectionPolicies/{information_protection_policy_name}'.format(scope='scope_example', information_protection_policy_name='information_protection_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_information_protection_policies_get(client):
    """Test case for information_protection_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Security/informationProtectionPolicies/{information_protection_policy_name}'.format(scope='scope_example', information_protection_policy_name='information_protection_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_information_protection_policies_list(client):
    """Test case for information_protection_policies_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Security/informationProtectionPolicies'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

