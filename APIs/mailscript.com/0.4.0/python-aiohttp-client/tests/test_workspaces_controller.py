# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_workspace_request import AddWorkspaceRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_workspaces_response import GetAllWorkspacesResponse


pytestmark = pytest.mark.asyncio

async def test_add_workspace(client):
    """Test case for add_workspace

    Claim a Mailscript workspace
    """
    body = {"workspace":"workspace"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/workspaces',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_workspaces(client):
    """Test case for get_all_workspaces

    Get all workspaces you have access to
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/workspaces',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

