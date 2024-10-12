# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user_for_workspace200_response import AddUserForWorkspace200Response
from openapi_server.models.add_user_for_workspace_request import AddUserForWorkspaceRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_workspace200_response import GetWorkspace200Response
from openapi_server.models.get_workspaces200_response import GetWorkspaces200Response
from openapi_server.models.remove_user_for_workspace_request import RemoveUserForWorkspaceRequest
from openapi_server.models.update_workspace_request import UpdateWorkspaceRequest


pytestmark = pytest.mark.asyncio

async def test_add_user_for_workspace(client):
    """Test case for add_user_for_workspace

    Add a user to a workspace or organization
    """
    body = openapi_server.AddUserForWorkspaceRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/workspaces/{workspace_gid}/addUser'.format(workspace_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspace(client):
    """Test case for get_workspace

    Get a workspace
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/workspaces/{workspace_gid}'.format(workspace_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspaces(client):
    """Test case for get_workspaces

    Get multiple workspaces
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/workspaces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_for_workspace(client):
    """Test case for remove_user_for_workspace

    Remove a user from a workspace or organization
    """
    body = openapi_server.RemoveUserForWorkspaceRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/workspaces/{workspace_gid}/removeUser'.format(workspace_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workspace(client):
    """Test case for update_workspace

    Update a workspace
    """
    body = openapi_server.UpdateWorkspaceRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/1.0/workspaces/{workspace_gid}'.format(workspace_gid='12345'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

