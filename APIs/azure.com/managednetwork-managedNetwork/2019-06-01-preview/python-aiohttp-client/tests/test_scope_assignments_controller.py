# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.scope_assignment import ScopeAssignment
from openapi_server.models.scope_assignment_list_result import ScopeAssignmentListResult


pytestmark = pytest.mark.asyncio

async def test_scope_assignments_create_or_update(client):
    """Test case for scope_assignments_create_or_update

    
    """
    parameters = {"properties":{"assignedManagedNetwork":"assignedManagedNetwork"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments/{scope_assignment_name}'.format(scope='scope_example', scope_assignment_name='scope_assignment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scope_assignments_delete(client):
    """Test case for scope_assignments_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments/{scope_assignment_name}'.format(scope='scope_example', scope_assignment_name='scope_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scope_assignments_get(client):
    """Test case for scope_assignments_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments/{scope_assignment_name}'.format(scope='scope_example', scope_assignment_name='scope_assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scope_assignments_list(client):
    """Test case for scope_assignments_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.ManagedNetwork/scopeAssignments'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

