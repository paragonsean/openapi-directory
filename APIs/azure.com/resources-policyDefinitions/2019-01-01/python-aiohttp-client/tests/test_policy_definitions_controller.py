# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.policy_definition import PolicyDefinition
from openapi_server.models.policy_definition_list_result import PolicyDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_create_or_update(client):
    """Test case for policy_definitions_create_or_update

    Creates or updates a policy definition in a subscription.
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"mode":"mode","metadata":"{}","policyRule":"{}","displayName":"displayName","policyType":"NotSpecified","description":"description","parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policyDefinitions/{policy_definition_name}'.format(policy_definition_name='policy_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_create_or_update_at_management_group(client):
    """Test case for policy_definitions_create_or_update_at_management_group

    Creates or updates a policy definition in a management group.
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"mode":"mode","metadata":"{}","policyRule":"{}","displayName":"displayName","policyType":"NotSpecified","description":"description","parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policyDefinitions/{policy_definition_name}'.format(policy_definition_name='policy_definition_name_example', management_group_id='management_group_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_delete(client):
    """Test case for policy_definitions_delete

    Deletes a policy definition in a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policyDefinitions/{policy_definition_name}'.format(policy_definition_name='policy_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_delete_at_management_group(client):
    """Test case for policy_definitions_delete_at_management_group

    Deletes a policy definition in a management group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policyDefinitions/{policy_definition_name}'.format(policy_definition_name='policy_definition_name_example', management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_get(client):
    """Test case for policy_definitions_get

    Retrieves a policy definition in a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policyDefinitions/{policy_definition_name}'.format(policy_definition_name='policy_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_get_at_management_group(client):
    """Test case for policy_definitions_get_at_management_group

    Retrieve a policy definition in a management group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policyDefinitions/{policy_definition_name}'.format(policy_definition_name='policy_definition_name_example', management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_get_built_in(client):
    """Test case for policy_definitions_get_built_in

    Retrieves a built-in policy definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Authorization/policyDefinitions/{policy_definition_name}'.format(policy_definition_name='policy_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_list(client):
    """Test case for policy_definitions_list

    Retrieves policy definitions in a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policyDefinitions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_list_built_in(client):
    """Test case for policy_definitions_list_built_in

    Retrieve built-in policy definitions
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Authorization/policyDefinitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_definitions_list_by_management_group(client):
    """Test case for policy_definitions_list_by_management_group

    Retrieve policy definitions in a management group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policyDefinitions'.format(management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

