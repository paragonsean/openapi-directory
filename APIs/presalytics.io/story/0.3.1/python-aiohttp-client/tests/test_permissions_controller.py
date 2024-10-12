# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.permission_type import PermissionType
from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_story_id_collaborators_userid_permissiontype_get(client):
    """Test case for story_id_collaborators_userid_permissiontype_get

    Permissions: Story Authorization for a User
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/collaborators/authorize/{story_collaborator_userid}/{permissiontype}'.format(id='id_example', story_collaborator_userid='story_collaborator_userid_example', permissiontype='permissiontype_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_permission_types_get(client):
    """Test case for story_permission_types_get

    Permissions: List Permission Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/permission_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

