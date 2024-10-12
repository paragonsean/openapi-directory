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
    assignment = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"None"},"properties":{"resourceGroups":{"key":{"name":"name","location":"location"}},"provisioningState":"creating","blueprintId":"blueprintId","locks":{"mode":"None"},"parameters":{"key":{"description":"description"}},"status":{"timeCreated":"timeCreated","lastModified":"lastModified"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}'.format(subscription_id='subscription_id_example', assignment_name='assignment_name_example'),
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}'.format(subscription_id='subscription_id_example', assignment_name='assignment_name_example'),
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}'.format(subscription_id='subscription_id_example', assignment_name='assignment_name_example'),
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Blueprint/blueprintAssignments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

