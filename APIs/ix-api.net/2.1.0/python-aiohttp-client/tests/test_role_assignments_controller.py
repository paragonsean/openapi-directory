# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.role_assignment import RoleAssignment
from openapi_server.models.role_assignment_request import RoleAssignmentRequest
from openapi_server.models.role_assignments_create400_response import RoleAssignmentsCreate400Response


pytestmark = pytest.mark.asyncio

async def test_role_assignments_create(client):
    """Test case for role_assignments_create

    
    """
    body = {"role":"role:23","contact":"contact:42b"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/role-assignments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_assignments_destroy(client):
    """Test case for role_assignments_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/role-assignments/{assignment_id}'.format(assignment_id='assignment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_assignments_list(client):
    """Test case for role_assignments_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('contact', 'contact_example'),
                    ('role', 'role_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/role-assignments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_assignments_read(client):
    """Test case for role_assignments_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/role-assignments/{assignment_id}'.format(assignment_id='assignment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

