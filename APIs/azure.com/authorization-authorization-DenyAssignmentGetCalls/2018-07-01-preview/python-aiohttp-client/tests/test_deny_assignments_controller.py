# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deny_assignment import DenyAssignment
from openapi_server.models.deny_assignment_list_result import DenyAssignmentListResult


pytestmark = pytest.mark.asyncio

async def test_deny_assignments_get(client):
    """Test case for deny_assignments_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Authorization/denyAssignments/{deny_assignment_id}'.format(scope='scope_example', deny_assignment_id='deny_assignment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deny_assignments_get_by_id(client):
    """Test case for deny_assignments_get_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{deny_assignment_id}'.format(deny_assignment_id='deny_assignment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deny_assignments_list(client):
    """Test case for deny_assignments_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Authorization/denyAssignments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deny_assignments_list_for_resource(client):
    """Test case for deny_assignments_list_for_resource

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/{resource_provider_namespace}/{parent_resource_path}/{resource_type}/{resource_name}/providers/Microsoft.Authorization/denyAssignments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_provider_namespace='resource_provider_namespace_example', parent_resource_path='parent_resource_path_example', resource_type='resource_type_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deny_assignments_list_for_resource_group(client):
    """Test case for deny_assignments_list_for_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Authorization/denyAssignments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deny_assignments_list_for_scope(client):
    """Test case for deny_assignments_list_for_scope

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Authorization/denyAssignments'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

