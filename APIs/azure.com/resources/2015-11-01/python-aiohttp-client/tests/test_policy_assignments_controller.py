# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.policy_assignment import PolicyAssignment
from openapi_server.models.policy_assignment_list_result import PolicyAssignmentListResult


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_create(client):
    """Test case for policy_assignments_create

    
    """
    parameters = {"name":"name","properties":{"policyDefinitionId":"policyDefinitionId","displayName":"displayName","scope":"scope"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy_assignment_name}'.format(scope='scope_example', policy_assignment_name='policy_assignment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_create_by_id(client):
    """Test case for policy_assignments_create_by_id

    
    """
    parameters = {"name":"name","properties":{"policyDefinitionId":"policyDefinitionId","displayName":"displayName","scope":"scope"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{policy_assignment_id}'.format(policy_assignment_id='policy_assignment_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_delete(client):
    """Test case for policy_assignments_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy_assignment_name}'.format(scope='scope_example', policy_assignment_name='policy_assignment_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_delete_by_id(client):
    """Test case for policy_assignments_delete_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{policy_assignment_id}'.format(policy_assignment_id='policy_assignment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_get(client):
    """Test case for policy_assignments_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy_assignment_name}'.format(scope='scope_example', policy_assignment_name='policy_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_get_by_id(client):
    """Test case for policy_assignments_get_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{policy_assignment_id}'.format(policy_assignment_id='policy_assignment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_list(client):
    """Test case for policy_assignments_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/policyAssignments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_list_for_resource(client):
    """Test case for policy_assignments_list_for_resource

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/{resource_provider_namespace}/{parent_resource_path}/{resource_type}/{resource_nameprovider}/Microsoft.Authorization/policyAssignments'.format(resource_group_name='resource_group_name_example', resource_provider_namespace='resource_provider_namespace_example', parent_resource_path='parent_resource_path_example', resource_type='resource_type_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_list_for_resource_group(client):
    """Test case for policy_assignments_list_for_resource_group

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Authorization/policyAssignments'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_assignments_list_for_scope(client):
    """Test case for policy_assignments_list_for_scope

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Authorization/policyAssignments'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

