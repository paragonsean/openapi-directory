# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.policy_set_definition import PolicySetDefinition
from openapi_server.models.policy_set_definition_list_result import PolicySetDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_create_or_update(client):
    """Test case for policy_set_definitions_create_or_update

    Creates or updates a policy set definition.
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"metadata":"{}","policyDefinitionGroups":[{"displayName":"displayName","name":"name","description":"description","category":"category","additionalMetadataId":"additionalMetadataId"},{"displayName":"displayName","name":"name","description":"description","category":"category","additionalMetadataId":"additionalMetadataId"}],"displayName":"displayName","policyType":"NotSpecified","description":"description","policyDefinitions":[{"groupNames":["groupNames","groupNames"],"policyDefinitionId":"policyDefinitionId","policyDefinitionReferenceId":"policyDefinitionReferenceId","parameters":{"key":{"value":"{}"}}},{"groupNames":["groupNames","groupNames"],"policyDefinitionId":"policyDefinitionId","policyDefinitionReferenceId":"policyDefinitionReferenceId","parameters":{"key":{"value":"{}"}}}],"parameters":{"key":{"allowedValues":["{}","{}"],"metadata":{"key":"{}"},"defaultValue":"{}","type":"String"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policySetDefinitions/{policy_set_definition_name}'.format(policy_set_definition_name='policy_set_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_create_or_update_at_management_group(client):
    """Test case for policy_set_definitions_create_or_update_at_management_group

    Creates or updates a policy set definition.
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"metadata":"{}","policyDefinitionGroups":[{"displayName":"displayName","name":"name","description":"description","category":"category","additionalMetadataId":"additionalMetadataId"},{"displayName":"displayName","name":"name","description":"description","category":"category","additionalMetadataId":"additionalMetadataId"}],"displayName":"displayName","policyType":"NotSpecified","description":"description","policyDefinitions":[{"groupNames":["groupNames","groupNames"],"policyDefinitionId":"policyDefinitionId","policyDefinitionReferenceId":"policyDefinitionReferenceId","parameters":{"key":{"value":"{}"}}},{"groupNames":["groupNames","groupNames"],"policyDefinitionId":"policyDefinitionId","policyDefinitionReferenceId":"policyDefinitionReferenceId","parameters":{"key":{"value":"{}"}}}],"parameters":{"key":{"allowedValues":["{}","{}"],"metadata":{"key":"{}"},"defaultValue":"{}","type":"String"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policySetDefinitions/{policy_set_definition_name}'.format(policy_set_definition_name='policy_set_definition_name_example', management_group_id='management_group_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_delete(client):
    """Test case for policy_set_definitions_delete

    Deletes a policy set definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policySetDefinitions/{policy_set_definition_name}'.format(policy_set_definition_name='policy_set_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_delete_at_management_group(client):
    """Test case for policy_set_definitions_delete_at_management_group

    Deletes a policy set definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policySetDefinitions/{policy_set_definition_name}'.format(policy_set_definition_name='policy_set_definition_name_example', management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_get(client):
    """Test case for policy_set_definitions_get

    Retrieves a policy set definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policySetDefinitions/{policy_set_definition_name}'.format(policy_set_definition_name='policy_set_definition_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_get_at_management_group(client):
    """Test case for policy_set_definitions_get_at_management_group

    Retrieves a policy set definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policySetDefinitions/{policy_set_definition_name}'.format(policy_set_definition_name='policy_set_definition_name_example', management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_get_built_in(client):
    """Test case for policy_set_definitions_get_built_in

    Retrieves a built in policy set definition.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Authorization/policySetDefinitions/{policy_set_definition_name}'.format(policy_set_definition_name='policy_set_definition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_list(client):
    """Test case for policy_set_definitions_list

    Retrieves the policy set definitions for a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policySetDefinitions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_list_built_in(client):
    """Test case for policy_set_definitions_list_built_in

    Retrieves built-in policy set definitions.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Authorization/policySetDefinitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_set_definitions_list_by_management_group(client):
    """Test case for policy_set_definitions_list_by_management_group

    Retrieves all policy set definitions in management group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementgroups/{management_group_id}/providers/Microsoft.Authorization/policySetDefinitions'.format(management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

