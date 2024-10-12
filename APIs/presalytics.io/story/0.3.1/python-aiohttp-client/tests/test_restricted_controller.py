# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collaborator_bulk_update_request import CollaboratorBulkUpdateRequest
from openapi_server.models.permission_type import PermissionType
from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_collaborators_post(client):
    """Test case for collaborators_post

    Collborators: Bulk Update (Admin Only)
    """
    body = openapi_server.CollaboratorBulkUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/collaborators',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

