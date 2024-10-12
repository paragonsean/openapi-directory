# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_workspace_membership200_response import GetWorkspaceMembership200Response
from openapi_server.models.get_workspace_memberships_for_user200_response import GetWorkspaceMembershipsForUser200Response


pytestmark = pytest.mark.asyncio

async def test_get_workspace_membership(client):
    """Test case for get_workspace_membership

    Get a workspace membership
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
        path='/api/1.0/workspace_memberships/{workspace_membership_gid}'.format(workspace_membership_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspace_memberships_for_user(client):
    """Test case for get_workspace_memberships_for_user

    Get workspace memberships for a user
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
        path='/api/1.0/users/{user_gid}/workspace_memberships'.format(user_gid='me'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workspace_memberships_for_workspace(client):
    """Test case for get_workspace_memberships_for_workspace

    Get the workspace memberships for a workspace
    """
    params = [('user', 'me'),
                    ('opt_pretty', true),
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
        path='/api/1.0/workspaces/{workspace_gid}/workspace_memberships'.format(workspace_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

