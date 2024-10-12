# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.assignment_list import AssignmentList


pytestmark = pytest.mark.asyncio

async def test_assignments_create_or_update(client):
    """Test case for assignments_create_or_update

    
    """
    assignment = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"None"},"properties":{"resourceGroups":{"key":{"name":"name","location":"location"}},"provisioningState":"creating","blueprintId":"blueprintId","locks":{"mode":"None","excludedPrincipals":["excludedPrincipals","excludedPrincipals"]},"parameters":{"key":{"reference":{"secretName":"secretName","keyVault":{"id":"id"},"secretVersion":"secretVersion"},"value":"{}"}},"status":{"managedResources":["managedResources","managedResources"]}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}'.format(scope='scope_example', assignment_name='assignment_name_example'),
        headers=headers,
        json=assignment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assignments_delete(client):
    """Test case for assignments_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}'.format(scope='scope_example', assignment_name='assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assignments_get(client):
    """Test case for assignments_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}'.format(scope='scope_example', assignment_name='assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assignments_list(client):
    """Test case for assignments_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprintAssignments'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

