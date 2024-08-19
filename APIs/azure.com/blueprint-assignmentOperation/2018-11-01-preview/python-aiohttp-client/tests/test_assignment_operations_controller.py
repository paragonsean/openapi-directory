# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assignment_operation import AssignmentOperation
from openapi_server.models.assignment_operation_list import AssignmentOperationList


pytestmark = pytest.mark.asyncio

async def test_assignment_operations_get(client):
    """Test case for assignment_operations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}/assignmentOperations/{assignment_operation_name}'.format(scope='scope_example', assignment_name='assignment_name_example', assignment_operation_name='assignment_operation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assignment_operations_list(client):
    """Test case for assignment_operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignment_name}/assignmentOperations'.format(scope='scope_example', assignment_name='assignment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

